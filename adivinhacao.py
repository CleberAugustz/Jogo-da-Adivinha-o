import random

def jogar_adivinhacao():
    print("*" * 10)
    print("Bem vindo ao jogo de Adivinhação")
    print("*" * 10)

    # numero_secreto = round(random.random()) # Gera número random entre 0.0 e 1.0
    numero_secreto = round(random.randrange(1, 101))  # Gera um número random com determinado range
    total_de_tentativas = 0
    score = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_user = int(input("Digite o seu número: "))

        print("Você digitou ", chute_user)
        acertou = chute_user == numero_secreto
        menor = chute_user < numero_secreto
        maior = chute_user > numero_secreto
        if (chute_user < 1 or chute_user > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute_user)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo!")

    if(__name__ == "__main__"):
        jogar_adivinhacao()