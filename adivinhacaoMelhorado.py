import random
#cores no terminal
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"

def escolher_nivel():
    print (VERDE+"\nEscolha o nível:")
    print(VERDE+"1- Fácil (15 tentativas)"+RESET)
    print(AMARELO+"2- médio (10 tentativas)"+RESET)
    print(VERMELHO+"1- hard (5 tentativas)"+RESET)

    while True:
        nivel_str = input("digite apenas números(1,2,3): ")
        if not nivel_str.isdigit():
            print (VERMELHO+" Digite apenas números! "+ RESET)
            continue
        nivel = int (nivel_str)
        if nivel == 1:
            return 15
        elif nivel == 2:
            return 10
        elif nivel == 3:
            return 5
        else:
            print (VERMELHO4+"Escolha apenas 1, 2 ou 3"+RESET)


def jogar():
    print(AZUL+"*********************************"+RESET)
    print(AZUL+"*******JOGO DE ADIVINHAÇÃO*******"+RESET)
    print(AZUL+"*********************************"+RESET)
    total_tentativas = escolher_nivel()
    numero_secreto = random.randrange(1,100)
    pontos = 100
    historico = []

    for rodada in range(1,total_tentativas + 1):
        #print("Tentativa {} de {}".format(rodada,total_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")

        if not chute_str.isdigit():
            print(VERMELHO+("Digite números entre 1 e 100:  ")+RESET)
            continue
        
        print("\nSeu chute é: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print(AMARELO+"Você deve digitar um número entre 1 e 100!"+RESET)
            continue
        historico.append(chute)
        
        if chute == numero_secreto:
            print (VERDE+"n\ Você acertou!"+RESET)
            print (VERDE+ f"Sua pontuacão foi: {pontos} pontos"+RESET)
            break
        else:
            pontos -=20
            if chute > numero_secreto:
                print (VERMELHO+"\n O número secreto é MAIOR"+RESET)
            else:
                print(VERMELHO+"\nO número secreto é MENOR"+RESET)
    else:
        print(VERMELHO+ f"\n Você perdeu! O número secreto era: {numero_secreto}"+RESET)
    print (AZUL+"históricio de tentativas: "+RESET,historico)
    print (AZUL+"FIM DE JOGO!"+RESET)

while True:
    jogar()
    repetir = input("\n Deseja jogar novamene? (s/n)").lower()
    
    if repetir !="s":
        print (AZUL+"Obrigado por jogar"+RESET)
        break