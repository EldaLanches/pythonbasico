while True:
    try:
        produtos = int(input("Digite a quantidade de produtos:"))
        if produtos <=0:
            print ("Deve ser maior que zero.")
        else:
            break
    except ValueError:
        print ("Digite apenas números inteiros.")

print ("Produtos cadastrados: ", produtos)