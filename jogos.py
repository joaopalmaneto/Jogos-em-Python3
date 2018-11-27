import forca
import adivinhacao


print("\nBEM VINDO AO MENU DE JOGOS!\n*******************************\n")
escolha = input("1- Forca\n2- Advinhação\nEscolha um jogo: ")

if(escolha == '1'):
    forca.jogar()
elif(escolha == '2'):
    adivinhacao.jogar()
