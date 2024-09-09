class ControllerLevel:
    def calcular_xp_para_proximo_nivel(self, level: int) -> int:
        return 50 * (level**2) + 50 * level

    def calcular_quanto_xp_falta_para_proximo_nivel(self, level: int, xp: int) -> int:
        return self.calcular_xp_para_proximo_nivel(level) - xp
