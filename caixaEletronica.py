while True:
    try:
        valor = int(input("Digite o valor do saque:"))
        if valor <=0:
            print ("O saque deve ser maior que zero.")
            continue
        elif valor >=1000:
            print("O saque deve ser menor que mil.")
            continue
        else:
            print (" saque efetuado.") 
            break
    except ValueError:
        print ("Digite apenas números inteiros.")

print ("Valor aceito: ", valor)