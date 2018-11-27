from time import sleep
import random

def jogar ():

    print("\nBem  vindo ao jogo da advinhação!!")
    print("************************************\n")


    x = 1 #variável apenas para iniciar o laço de repetição

    print("Escolha o nível de dificuldade: \n")
    nivel = int(input("(1) Fácil\n(2) Médio\n(3) Difícil\n"))

    if(nivel == 1):
        max = 30
        numero_secreto = random.randrange(0, 30) #numero que o usuario tentará descobrir
        tentativas = 10 #numero inicial de tentativas
        print("Você tem 10 tentativas!\n")
    elif(nivel == 2):
        max = 50
        numero_secreto = random.randrange(0, 50)  # numero que o usuario tentará descobrir
        tentativas = 7  # numero inicial de tentativas
        print("Você tem 7 tentativas!\n")

    elif(nivel == 3):
        max = 100
        numero_secreto = random.randrange(0, 100)  # numero que o usuario tentará descobrir
        tentativas = 5  # numero inicial de tentativas
        print("Você tem 5 tentativas!\n")
    else:
        print("ERRO: Esse não é um valor válido.")


    for x in range(tentativas): #inicia um laço de repetição para que o jogador possa ter várias tentativas

        chute = int(input("Digite um número entre 0 e {}: ".format(max))) #recebe a tentativa do usuario e a converte para valor do tipo inteiro

        if (chute < 1 or chute > max):
            print("ERRO: O número digitado deve ser entre 0 e {}. \n".format(max))
            continue

        sleep(1.5) #pequeno tempo de pausa

        acertou = numero_secreto == chute #armazena a igualdade entre o chute e o numero secreto
        acima = numero_secreto < chute #armazena que o numero secreto é maior que o chute
        abaixo = numero_secreto > chute #armazena que o numero secreto é menor que o chute

        if(acertou): #verifica se o numero digitado pelo usuario é igual ao numero secreto
            print("Você acertou, parabéns!!")
            break #em caso positivo, dirá ao usuário que ele acertou e o programa será finalizado

        else:
            if(acima):
                print("Você errou, tente um número menor\n")
            elif(abaixo):
                print("Você errou, tente um número maior\n")
            tentativas = tentativas - 1 #a cada rodada uma tentativa é subtraida
            print("Você tem {} tentativas !".format(tentativas))

    print("Fim do Jogo :(")

if(__name__ == '__main__'):
    jogar()