print('***********************************')
print('********jogo de adivinhação********')
print('***********************************')

numero_secreto = 39

chute_str = input("Digite o seu número:  ")

print("Seu número é: ", chute_str)

chute = int(chute_str)

if(numero_secreto == chute ):
    print("Você acertou!")
else:
    print("Você errou ;-; ")