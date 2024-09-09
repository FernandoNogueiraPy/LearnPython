from src.entities.challenges.challenge import ChallengeRandom
from src.repositories.challenges.connect_challenges_random import (
    respository_challenge_random_sync,
)


def random_challenge_one():
    id_challenge = "MAP_1_RANDOM_1"
    challenge_postion_random = 1
    mapa = "Vale das Variaveis"
    nome_desafio = "Desafio Aleatório: Manipulação de Strings"
    explication_desafio = """\n

    Em Python, você pode manipular strings de várias maneiras. Além de concatenar strings, você pode usar métodos como .upper(), .lower() e .replace() para alterar o conteúdo das strings.

    Considere o seguinte código:
    \n
    texto = "Olá, Mundo!"
    \ntexto_maiusculo = texto.upper()
    \n
    Aqui, texto_maiusculo será "OLÁ, MUNDO!". O método .upper() converte todos os caracteres da string para maiúsculas.

    """
    descricao_desafio = (
        "Qual será o resultado do código a seguir?\n\n"
        "texto = 'Python é divertido!'\n"
        "resultado = texto.replace('divertido', 'incrível')\n"
        "print(resultado)\n"
    )

    options = [
        "'Python é incrível!'",
        "'Python é divertido!'",
        "'Python é incrível'",
        "'Python é incrível!!'",
        "'Python é divertido'",
    ]

    return ChallengeRandom(
        id=id_challenge,
        challenge_postion_random=challenge_postion_random,
        difficulty=2,
        mapa=mapa,
        name=nome_desafio,
        explication=explication_desafio,
        description=descricao_desafio,
        points=2,
        exp=100.0,
        options=options,
    )
