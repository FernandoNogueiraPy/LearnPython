from pydantic import BaseModel
from typing import Literal

MAPS_NAME = Literal[
    "Vale das Variaveis",
    "Floresta de Condições",
    "Montanha dos Loops",
    "Deserto de Funções",
    "Oceano de Objetos",
]


class ChallengeInfo(BaseModel):
    total_challenges: int = 0
    total_points: int = 0
    total_completed: int = 0
    total_failed: int = 0


class HistoryChallengeCurrent(BaseModel):
    id_challenge: int
    challenge_name: str = "Desafio 1"
    challenge_points: int = 0
    challenge_completed: bool = False


class ModeChallengeHistory(BaseModel):
    maps_total: int = 5
    maps_completed: int = 0
    maps_peding: int = 5
    map_current: int = 1
    map_current_name: MAPS_NAME = "Vale das Variaveis"
    history_current: HistoryChallengeCurrent


class ChallengerInfo(BaseModel):
    id_player: str
    challenge_info: ChallengeInfo
    challenge_history: ModeChallengeHistory
