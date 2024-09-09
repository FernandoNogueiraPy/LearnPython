from src.entities.challenges.challenge import Challenge
# from src.repositories.challenges.connect_challenges_history import (
#    respository_challenge_history_sync,
# )


def challenge_one():
    id_challenge = "MAP_1_CHALLENGE_1"
    mapa = "Vale das Variaveis"
    nome_desafio = "Desafio: A primeira Variavel"
    explication_desafio = """\n

    Uma varivel é um espaço de memória que armazena um valor, que pode ser alterado durante a execução do programa.
    Para criar uma variável, você deve informar o nome da variável e o valor que deseja armazenar.
    \n
    \n
    Exemplo:\n
    \nnome = "João"
    \nidade = 25
    \n
    Neste exemplo, a variável nome armazena o valor "João" e a variável idade armazena o valor 25.
    O operador '=' é utilizado para atribuir um valor a uma variável.

    """
    descricao_desafio = (
        "Qual e o sinal de atribuição na linguagem de programação Python?"
    )

    options = ["x", "=>", "=", "==", "->", "==>", "->>", "==>>"]

    return Challenge(
        id=id_challenge,
        history_mode=True,
        challenge_postion_map=1,
        difficulty=1,
        mapa=mapa,
        name=nome_desafio,
        explication=explication_desafio,
        description=descricao_desafio,
        options=options,
        points=1,
        exp=75.0,
    )


def challenge_two():
    id_challenge = "MAP_1_CHALLENGE_2"
    mapa = "Vale das Variaveis"
    nome_desafio = "Desafio: Tipos de Dados Simples"
    explication_desafio = """\n

    Em Python, uma variável pode armazenar diferentes tipos de dados, como números inteiros, números de ponto flutuante, strings e booleanos.
    Os tipos de dados mais comuns são:
    - int: números inteiros
    - float: números com ponto flutuante
    - str: cadeias de caracteres (strings)
    - bool: valores booleanos (True ou False)

    Exemplo:
    \n
    numero_inteiro = 10
    \nnumero_decimal = 10.5
    \ntexto = "Olá Mundo"
    \nbooleano = True
    \n
    Neste exemplo, cada variável armazena um tipo diferente de dado.

    """
    descricao_desafio = "Qual tipo de dado é usado para armazenar números com ponto flutuante em Python?"

    options = ["int", "float", "str", "bool"]

    return Challenge(
        id=id_challenge,
        history_mode=True,
        challenge_postion_map=2,
        difficulty=1,
        mapa=mapa,
        name=nome_desafio,
        explication=explication_desafio,
        description=descricao_desafio,
        options=options,
        points=2,
        exp=100.0,
    )


def challenge_three():
    id_challenge = "MAP_1_CHALLENGE_3"
    mapa = "Vale das Variaveis"
    nome_desafio = "Desafio: Nomes de Variáveis"
    explication_desafio = """\n

    Em Python, ao criar nomes de variáveis, é importante seguir algumas regras:
    - O nome deve começar com uma letra (a-z, A-Z) ou um sublinhado (_).
    - Pode conter letras, números e sublinhados.
    - Não pode começar com um número.
    - Não pode ser uma palavra reservada da linguagem.

    Exemplos válidos:
    \n
    nome_usuario
    \nidade
    \n_telefone
    \n
    Exemplos inválidos:
    \n
    1nome
    \nif
    \n
    """
    descricao_desafio = (
        "Qual é uma das regras para criar um nome de variável válido em Python?"
    )

    options = [
        "Começar com um número",
        "Não pode conter letras no inicio",
        "Não pode ser uma palavra reservada",
        "Não pode conter sublinhados",
    ]

    return Challenge(
        id=id_challenge,
        history_mode=True,
        challenge_postion_map=3,
        difficulty=1,
        mapa=mapa,
        name=nome_desafio,
        explication=explication_desafio,
        description=descricao_desafio,
        options=options,
        points=1,
        exp=100.0,
    )


def challenge_four():
    id_challenge = "MAP_1_CHALLENGE_4"
    mapa = "Vale das Variaveis"
    nome_desafio = "Desafio: Operadores de Atribuição"
    explication_desafio = """\n

    Em Python, você pode usar operadores de atribuição para alterar o valor de uma variável.
    Os operadores mais comuns são:
    - =: Atribuição simples
    - +=: Adiciona e atribui
    - -=: Subtrai e atribui
    - *=: Multiplica e atribui
    - /=: Divide e atribui

    Exemplo:
    \n
    x = 10
    \nx += 5  # Agora x é 15
    \n
    O operador += adiciona 5 ao valor atual de x.

    """
    descricao_desafio = "Qual operador é usado para adicionar e atribuir um valor a uma variável em Python?"

    options = ["=", "+=", "-=", "*=", "/="]

    return Challenge(
        id=id_challenge,
        history_mode=True,
        challenge_postion_map=4,
        difficulty=1,
        mapa=mapa,
        name=nome_desafio,
        explication=explication_desafio,
        description=descricao_desafio,
        options=options,
        points=1,
        exp=75.0,
    )


def challenge_five():
    id_challenge = "MAP_1_CHALLENGE_5"
    mapa = "Vale das Variaveis"
    nome_desafio = "Desafio: Manipulação de Variáveis"
    explication_desafio = """\n

    Em Python, você pode manipular variáveis de várias maneiras. Um aspecto importante é o uso de variáveis para realizar operações matemáticas e concatenar strings.

    Considere o seguinte código:
    \n
    a = 5
    \nb = 3
    \nc = a + b
    \n
    Aqui, c armazena o resultado da soma de a e b. Agora, considere o seguinte exemplo com strings:
    \n
    nome = "Ana"
    \nidade = 30
    \nmensagem = nome + " tem " + str(idade) + " anos."
    \n
    Neste exemplo, a variável mensagem armazena uma string concatenada com o nome e a idade.

    """
    descricao_desafio = (
        "Qual é a saída do código a seguir?\n\n"
        "x = 10\n"
        "y = 5\n"
        "z = x * y + 2\n"
        "resultado = z / 3\n"
        "print(resultado)\n"
    )

    options = ["6.666666666666667", "7.0", "8.0", "10.0", "15.0", "17.3333"]

    return Challenge(
        id=id_challenge,
        history_mode=True,
        challenge_postion_map=5,
        difficulty=2,
        mapa=mapa,
        name=nome_desafio,
        explication=explication_desafio,
        description=descricao_desafio,
        options=options,
        points=3,
        exp=150.0,
    )


# def sync_challenges():
#     challenges = [
#         challenge_one(),
#         challenge_two(),
#         challenge_three(),
#         challenge_four(),
#         challenge_five(),
#     ]

#     for challenge in challenges:
#         respository_challenge_history_sync.insert_one(challenge)
