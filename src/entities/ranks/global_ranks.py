from pydantic import BaseModel


class TitleRanks(BaseModel):
    NOVATO: str = "Novato Tecnológico"
    AVENTUREIRO: str = "Aventureiro Digital"
    EXPLORADOR: str = "Explorador de Bits"
    DESBRAVADOR: str = "Desbravador de Códigos"
    MESTRE: str = "Mestre da Programação"
    LENDA: str = "Lenda do Código"
    AS_PROGRAMACAO: str = "Ás da Programação"


class PointsToRank(BaseModel):
    NOVATO: int = 0  # 0 a 50
    AVENTUREIRO: int = 51  # 51 a 100
    EXPLORADOR: int = 101  # 101 a 200
    DESBRAVADOR: int = 201  # 201 a 350
    MESTRE: int = 351  # 351 a 500
    LENDA: int = 501  # 501 a 1000
    AS_PROGRAMACAO: int = 1000  # 1000 NO LIMIT
