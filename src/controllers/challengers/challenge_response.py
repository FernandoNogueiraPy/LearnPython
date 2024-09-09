from src.entities.rewards.reward_challenge import RewardsChallenge
from src.entities.challenges.challenge_response import ChallengeReponseUser
from src.entities.challenges.challenge_response import ResponseChallengeApp

from src.controllers.challengers.history.challenges_map_1 import challenge_one


def response_challenge_one(response: ChallengeReponseUser) -> ResponseChallengeApp:
    if not response.id_challenge == "CHALLENGE_1":
        raise ValueError("Challenge not found")

    challenge = challenge_one()

    explication_response = (
        "O sinal de atribuição na linguagem de programação Python é o '='"
    )

    if response.response_user == "=":
        recompensa = RewardsChallenge(
            id_challenge=response.id_challenge,
            id_player=response.id_player,
            name_reward=challenge.name,
            **challenge.model_dump(),
        )

        return ResponseChallengeApp(
            message="Parabéns, você acertou!",
            description=explication_response,
            next_challenge=True,
            reward=recompensa,
        )

    return ResponseChallengeApp(
        message="Que pena, você errou!",
        description=explication_response,
        next_challenge=False,
    )
