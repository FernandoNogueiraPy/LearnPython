from addemongo import QueryBuilder

from src.services.level.controller_level import ControllerLevel
from src.entities.rewards.reward_challenge import RewardsChallenge
from src.entities.challenges.challenge_overview import ChallengeOverview, ChallengeInfo
from src.entities.ranks.player_rank import PlayerRank, PlayerExp
from src.entities.ranks.global_ranks import PointsToRank, TitleRanks

from src.repositories.challenges.connect_challenge_overview import (
    respository_challenge_overview_sync,
)


class ControllerRawards:
    def apply_reward(self, reward: RewardsChallenge):
        query = QueryBuilder()
        query.set_equal("id_player", reward.id_player)
        player_overview = respository_challenge_overview_sync.find_one(query)

        if not player_overview:
            raise ValueError("Player not found")

        self.__reward_ranking(reward, player_overview)

        respository_challenge_overview_sync.update_one(query, player_overview)

    def __reward_ranking(
        self, reward: RewardsChallenge, player_overview: ChallengeOverview
    ):
        info_player = player_overview.challenge_info
        info_level = player_overview.player_rank.info_level
        info_rank = player_overview.player_rank

        if reward.complete_challenge:
            info_player = self.__apply_up_points(reward, info_player)
            info_level = self.__apply_up_level(reward, info_level)

        else:
            info_player = self.__apply_down_points(reward, info_player)
            info_level = self.__apply_down_level(reward, info_level)

        info_rank = self.__apply_ranking(info_player.total_points, info_rank)

        return player_overview

    def __apply_up_points(self, reward: RewardsChallenge, info_player: ChallengeInfo):
        info_player.total_points += reward.points
        info_player.total_challenges += 1

        if reward.complete_challenge:
            info_player.total_completed += 1
        else:
            info_player.total_failed += 1

        return info_player

    def __apply_up_level(self, reward: RewardsChallenge, info_level: PlayerExp):
        controller_level = ControllerLevel()

        level_player_current = info_level.level
        xp_next_level = controller_level.calcular_xp_para_proximo_nivel(
            level_player_current
        )

        if xp_next_level < (info_level.exp_current + reward.exp):
            info_level.level += 1

        info_level.exp_current += reward.exp
        info_level.exp_next_level = controller_level.calcular_xp_para_proximo_nivel(
            info_level.level
        )

        return info_level

    def __apply_down_points(self, reward: RewardsChallenge, info_player: ChallengeInfo):
        info_player.total_points -= reward.points
        info_player.total_challenges += 1
        info_player.total_failed += 1

        return info_player

    def __apply_down_level(self, reward: RewardsChallenge, info_level: PlayerExp):
        controller_level = ControllerLevel()

        level_player_current = info_level.level

        xp_minor_level = controller_level.calcular_xp_para_proximo_nivel(
            level_player_current - 1
        )

        if (info_level.exp_current - reward.exp) < xp_minor_level:
            info_level.level -= 1

        info_level.exp_current -= reward.exp
        info_level.exp_next_level = controller_level.calcular_xp_para_proximo_nivel(
            info_level.level
        )

        return info_level

    def __apply_ranking(self, points_current: int, info_rank: PlayerRank):
        dict_ranks = PointsToRank().model_dump()

        if points_current > 1000:
            info_rank.rank_current = TitleRanks.AS_PROGRAMACAO
            return info_rank

        for title, points in dict_ranks.items():
            if points_current > points:
                pass
            else:
                info_rank.rank_current = TitleRanks().model_dump()[title]
                break

        return info_rank
