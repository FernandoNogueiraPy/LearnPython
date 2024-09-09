from pydantic import BaseModel

from src.entities.maps.mapas import MAPS_NAME
from src.entities.ranks.player_rank import PlayerRank


class ChallengeInfo(BaseModel):
    total_challenges: int = 0
    total_points: int = 0
    total_completed: int = 0
    total_failed: int = 0


class HistoryChallengeCurrent(BaseModel):
    id_challenge: str = "MAP_1_CHALLENGE_1"
    challenge_name: str = "Desafio: A primeira Variavel"
    challenge_position_in_map: int = 1
    challenge_points: int = 0
    challenge_completed: bool = False


class ModeChallengeHistory(BaseModel):
    maps_total: int = 5
    maps_completed: int = 0
    maps_peding: int = 5
    map_current: int = 1
    map_current_name: str = "Vale das Variaveis"
    history_current: HistoryChallengeCurrent = HistoryChallengeCurrent()


class ChallengeOverview(BaseModel):
    id_player: str
    username: str
    player_rank: PlayerRank = PlayerRank()
    challenge_info: ChallengeInfo = ChallengeInfo()
    challenge_history: ModeChallengeHistory = ModeChallengeHistory()
