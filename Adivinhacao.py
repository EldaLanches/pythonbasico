print('***********************************')
print('********jogo de adivinhação********')
print('***********************************')

numero_secreto = 39
total_tentativas = 3
rodada = 1

while(rodada <=total_tentativas):
    chute_str = input("Digite o seu número:  ")
    print("Seu número é: ", chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou ):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Seu chute foi maior que o número secreto.")
        elif(menor):
            print("Seu chute foi menor que o número secreto.")
        print("Você errou ;-; ")
    rodada = rodada +1

print("Fim de jogo")