from pydantic import BaseModel


class TitleRanks(BaseModel):
    NOVATO: str = "Novato Tecnológico"
    AVENTUREIRO: str = "Aventureiro Digital"
    EXPLORADOR: str = "Explorador de Bits"
    DESBRAVADOR: str = "Desbravador de Códigos"
    MESTRE: str = "Mestre da Programação"
    LENDA: str = "Lenda do Código"
    AS_PROGRAMACAO: str = "Ás da Programação"
