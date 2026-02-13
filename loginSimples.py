while True:
    nome = input("Digite seu nome: ").strip()
    if nome == "":
        print("O nome não pode ser vazio.")
        continue

    senha = input("Digite sua senha: ").strip()
    if len(senha) < 6:
        print("A senha deve ter no mínimo 6 caracteres.")
        continue

    print("Login cadastrado com sucesso!")
    break
