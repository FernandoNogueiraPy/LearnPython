from addemongo import QueryBuilder

from src.entities.rewards.reward_challenge import RewardsChallenge
from src.entities.challenges.challenge_response import (
    ChallengeReponseUser,
    ResponseChallengeApp,
    ResponseChallengeCorrect,
)

<<<<<<< HEAD:src/services/challengers/challenge_response.py
from src.services.challengers.history.challenges_map_1 import challenge_one
=======
from src.controllers.rewards.controller_rewards import ControllerRawards

from src.repositories.challenges.connect_responses import (
    respository_challenge_response_sync,
)
from src.repositories.challenges.connect_challenges_random import (
    respository_challenge_random_sync,
)
from src.repositories.challenges.connect_challenges_history import (
    respository_challenge_history_sync,
)
>>>>>>> ede1bf39575fdd3e6171b69638473a1e56a609e8:src/controllers/challengers/challenge_response.py


class ControllerChallengeResponse:
    def check_response(
        self, response: ChallengeReponseUser, mode_history: bool
    ) -> ResponseChallengeApp:
        response_in_database = self.search_response(response.id_challenge)

        query = QueryBuilder()
        query.set_equal("id", response.id_challenge)

        if mode_history:
            challenge = respository_challenge_history_sync.find_one(query)
        else:
            challenge = respository_challenge_random_sync.find_one(query)

        if not challenge:
            raise ValueError("Challenge not found")

        if response.response_user == response_in_database.response_correct:
            message_response = "Parabéns, você acertou!"
            next_challenge_now = True

        else:
            message_response = "Que pena, você errou!"
            next_challenge_now = False

        recompensa = RewardsChallenge(
            id_challenge=response.id_challenge,
            id_player=response.id_player,
            name_reward=challenge.name,
            complete_challenge=next_challenge_now,
            **challenge.model_dump(),
        )

        controller_rewards = ControllerRawards()
        controller_rewards.apply_reward(recompensa)

        responses = ResponseChallengeApp(
            message=message_response,
            description=response_in_database.explication_response,
            next_challenge=next_challenge_now,
            reward=recompensa,
        )

        return responses

    def search_response(self, id_challenge: str) -> ResponseChallengeCorrect:
        query = QueryBuilder()
        query.set_equal("id_challenge", id_challenge)

        response_challenge = respository_challenge_response_sync.find_one(query)

        if response_challenge:
            return response_challenge

        raise ValueError("Response Challenge not found")
