import forca
import adivinhacao
import os

def escolhe_jogo():
    while(True):
        os.system('clear') or None
        print("*********************************")
        print("*******Escolha o seu jogo!*******")
        print("*********************************")

        print("(1) Forca (2) Adivinhação")

        jogo = int(input("Qual jogo?"))

        if(jogo == 1):
            print("Jogando Forca")
            forca.jogar()
        elif(jogo == 2):
            print("Jogando Adivinhação")
            adivinhacao.jogar()
        print("Pressione Enter para continuar ou Ctrl+Z para encerrar....")
        input()
if(__name__ == "__main__"):
    escolhe_jogo()
