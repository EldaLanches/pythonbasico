while True:
    try:
        nascimento = float(input("Digite seu nascimento:"))
        if 1900<= nascimento <=2026:
            break
        else:
            print("O nascimento deve estar entre 1900 e 2026. ")
    except ValueError:
        print ("Digite apenas números inteiros.")

print ("nascimento Cadastrado: ", nascimento)
