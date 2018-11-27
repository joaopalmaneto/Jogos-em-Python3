import random

def sortear_palavra():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    escolhida = palavras[random.randrange(0, len(palavras))]
    arquivo.close()

    return escolhida


def mensagem_final(acertou):
    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu :(")
    print("Fim do Jogo")


def jogar():
    print("\nBem  vindo ao jogo da Forca!!")
    print("*******************************\n")


    palavra_secreta = sortear_palavra().lower()
    acertou = False
    enforcou = False
    exibicao = ['_' for letra in palavra_secreta]
    erros = 0

    print(exibicao)

    while(not enforcou and not acertou):
        index = 0
        chute = input("\nDigite uma letra: ").strip()
        if(chute.lower() in palavra_secreta.lower()):
            for letras in palavra_secreta:
                if letras.lower() == chute.lower():
                    exibicao[index] =  chute.lower()
                index += 1
            print(exibicao)
            #torna "acertou" verdadeira caso não haja nenhum underscore restando
            acertou = "_" not in exibicao

        else:
            erros += 1
            enforcou = erros == 5
            print("Tentativas = {}".format(5 - erros))

    mensagem_final(acertou)

if(__name__ == '__main__'):
    jogar()


