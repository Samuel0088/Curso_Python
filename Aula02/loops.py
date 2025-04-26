def aplicacao():
    senha = 0 
    try:
        senha = int(input("Digite a senha: "))
        while (senha != 2002):
            senha = int(input("Senha inválida, tente novamente: "))
        print("Acesso permitido!")
    except ValueError:
        print("Valor inválido de senha, tente somente números")

aplicacao()