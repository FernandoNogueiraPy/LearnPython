class ControllerLevel:
    def calcular_xp_para_proximo_nivel(self, level: int) -> int:
        return 50 * (level**2) + 50 * level

    def calcular_quanto_xp_falta_para_proximo_nivel(self, level: int, xp: int) -> int:
        return self.calcular_xp_para_proximo_nivel(level) - xp


teste_level = ControllerLevel()

print(teste_level.calcular_quanto_xp_falta_para_proximo_nivel(5, 0))
# Novato


print(teste_level.calcular_quanto_xp_falta_para_proximo_nivel(10, 1500))
# Aventureito

print(teste_level.calcular_quanto_xp_falta_para_proximo_nivel(17, 4000))
