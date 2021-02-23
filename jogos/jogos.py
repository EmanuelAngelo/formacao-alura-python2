import forca
import adivinhacao

def escolhe_jogo():
    print("**********************************")
    print("Bem vindo escolha um GAME!")
    print("**********************************")
    print("\n Escolha um dos jogos \n (1) Adivinhação \n (2) Forca")

    jogo = int(input("Qual jogo: "))
    if (jogo == 1):
        print("Adivinhação")
        adivinhacao.jogar()
    elif (jogo ==2):
        print("Forca")
        forca.jogar()
if (__name__ == "__main__"):
    escolhe_jogo()