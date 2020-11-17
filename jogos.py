import forca
import adivinhacao

def escolher_jogos():
    ast_identacao = 28
    print("*" * ast_identacao)
    print("****Escolha o seu jogo***")
    print("*" * ast_identacao)

    print("(1) Forca (2) Adivinhação")
    select = int(input("Qual jogo? "))

    if (select == 1):
        print("Jogando Forca")
        forca.jogar_forca()
    else:
        print("Jogando Adivinhação")
        adivinhacao.jogar_adivinhacao()

    print("Fim do jogo!")

if (__name__ == "__main__"):
    escolher_jogos()