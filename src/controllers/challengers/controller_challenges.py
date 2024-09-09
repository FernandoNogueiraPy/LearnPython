from addemongo import QueryBuilder
from fastapi import HTTPException
from random import choice

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

    def active_challenge(self, id_player: int, mode_history: bool):
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

    def history_challenge(self):
        pass
