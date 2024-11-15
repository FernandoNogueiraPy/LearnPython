from addemongo import QueryBuilder

from src.entities.challenges.challenge_overview import ChallengeOverview
from src.repositories.challenges.connect_challenge_overview import (
    respository_challenge_overview_sync,
)


class ControllerChallengeOverview:
    def __init__(self):
        self._challenge_overview = respository_challenge_overview_sync

    def create_challenge_overview(
        self, player_id: str, username: str
    ) -> ChallengeOverview:
        challenge_overview = ChallengeOverview(id_player=player_id, username=username)
        self._challenge_overview.insert_one(challenge_overview)
        return challenge_overview

    def get_challenge_overview(
        self, player_id: str, username: str
    ) -> ChallengeOverview:
        query = QueryBuilder()
        query.set_equal("id_player", player_id)
        query.set_equal("username", username)
        result = self._challenge_overview.find_one(query)

        if not result:
            return self.create_challenge_overview(player_id, username)

        return result
