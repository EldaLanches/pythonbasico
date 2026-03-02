import random
#cores no terminal
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"

def escolher_nivel():
    print ("\nEscolha o nível:")
    print("1- Fácil (15 tentativas)")
    print("2- médio (10 tentativas)")
    print("1- hard (5 tentativas)")

    while True:
        nivel_str = input("digite apenas números(1,2,3): ")
        if not nivel_str.isdigit():
            print (VERMELHO+" Digite apenas números! "+ RESET)
            continue
        nivel_str = int (nivel_str)
        if nivel == 1:
            return 15
        elif nivel == 2:
            return 10
        elif nivel == 3:
            return 5
        else:
            print (AMARELO+"Escolha apenas 1, 2 ou 3"+RESET)


def jogar():
    print(AZUL+"*********************************"+RESET)
    print(AZUL+"*******JOGO DE ADIVINHAÇÃO*******"+RESET)
    print(AZUL+"*********************************"+RESET)
    total_tentativas = escolher_nivel()
    numero_secreto = random.randrange(1,100)
    pontos = 100
    historico = []

    for rodada in range(1,total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada,total_tentativas))
        chute_str = input("DDigite um número entre 1 e 100: ")

        if not chute_str.isdigit():
            print(VERMELHO+("Digite números entre 1 e 100:  ")+RESET)
            continue

        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print(AMARELO+"Você deve digitar um número entre 1 e 100!"+RESET)
        continue
        




