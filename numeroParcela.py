while True:
    try:
        parcela = float(input("Digite sua parcela:"))
        if 1<= parcela <=12:
            break
        else:
            print("A parcela deve estar entre 1 e 12.")
    except ValueError:
        print ("Digite apenas números inteiros.")

print ("Parcela Cadastrada: ", parcela)
