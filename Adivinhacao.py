import random
print('***********************************')
print('********jogo de adivinhação********')
print('***********************************')

numero_secreto = random.randrange(1,100)
total_tentativas = 15
rodada = 1

for rodada in range(1,total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada,total_tentativas))

    chute_str = input("Digite o seu número:  ")
    print("Seu número é: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou ):
        print("---- Você acertou!----")
        break
    else:
        if(maior):
            print("**** Seu chute foi maior que o número secreto. ****")
        elif(menor):
            print("**** Seu chute foi menor que o número secreto. ****")
        print("---- Você errou ;-; ----")
    rodada = rodada +1

print("Fim de jogo")