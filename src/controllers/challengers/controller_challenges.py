from hmac import new
from addemongo import QueryBuilder
from fastapi import HTTPException
from random import choice

from entities.challenges.challenge_overview import ChallengeOverview
from src.entities.challenges.challenge_overview import HistoryChallengeCurrent
from src.entities.maps.mapas import MAPS_NAME_DICT, MAPS_NAME
from src.entities.challenges.challenge import ChallengeRandom
from src.repositories.challenges.connect_challenge_overview import (
    respository_challenge_overview_sync,
)

from src.repositories.challenges.connect_challenges_history import (
    respository_challenge_history_sync,
)

from src.repositories.challenges.connect_challenges_random import (
    respository_challenge_random_sync,
)


class ControllerChallenges:
    def __init__(self):
        self.overview_player = respository_challenge_overview_sync

        self.quantidade_challenges_random = (
            respository_challenge_random_sync.count_documents(QueryBuilder())
        )

    def active_challenge(self, id_player: str, mode_history: bool):
        querybuild = QueryBuilder()
        querybuild.set_equal("id_player", id_player)
        player_overview = self.overview_player.find_one(querybuild)

        if not player_overview:
            raise HTTPException(
                status_code=400,
                detail="Erro: O jogador não possui desafios ativos.",
            )

    def __balance_challenge(self):
        pass

    def random_challenge(self) -> ChallengeRandom:
        querybuild = QueryBuilder()
        querybuild.set_equal(
            "challenge_postion_random",
            choice([1, self.quantidade_challenges_random]),
        )

        desafio = respository_challenge_random_sync.find_one(querybuild)

        if not desafio:
            raise HTTPException(
                status_code=400,
                detail="Erro: Desafio não encontrado.",
            )

        return desafio

    def history_challenge(self, id_player: str):
        querybuild = QueryBuilder()
        querybuild.set_equal("id_player", id_player)
        player_overview = self.overview_player.find_one(querybuild)

        if not player_overview:
            raise HTTPException(
                status_code=400,
                detail="Erro: O jogador não possui desafios ativos.",
            )

    def __update_map_history(self, player_overview: ChallengeOverview):
        history_player = player_overview.challenge_history
        challenge_completed = history_player.history_current.challenge_completed

        if challenge_completed is True:
            maps_total = history_player.maps_total
            if history_player.history_current.challenge_position_in_map == maps_total:
                new_map = history_player.map_current + 1
                history_player.maps_completed += 1
                history_player.map_current = new_map
                history_player.map_current_name = MAPS_NAME_DICT[new_map]
                history_player.maps_peding = maps_total - new_map
                history_player.history_current.challenge_position_in_map = 1
              
            self.__update_challenge_history(history_player.history_current)

    def __update_challenge_history(self,challenge_currented:HistoryChallengeCurrent):
        
        if 