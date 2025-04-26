#Aluno: Samuel Vieira
def Aplicacao():
    try:
        while True:
            x = int(input("Digite um numero inteiro: "))
            i = 0
            if x == 0:
                break
            if x%2 != 0:
                x += 1
            soma = 0
            while (i < 5):
                soma += x
                x += 2
                i += 1
                print(x)
            print(f"SOMA: {soma}")
    except ValueError:
        print("Digite um número do tipo inteiro")

Aplicacao()