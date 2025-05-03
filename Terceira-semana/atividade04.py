#Aluno: Samuel Vieira
def leitor():
    try:
        numeros = int(input("Quantos números você vai digitar: "))
        for i in range(numeros):
            a = int(input("Digite um número: "))
            if a%2 == 0 and a < 0:
                print("PAR NEGATIVO")
            elif a%2 != 0 and a < 0:
                print("IMPAR NEGATIVO")
            elif a%2 == 0 and a > 0:
                print("PAR POSITIVO")
            elif a%2 != 0 and a > 0:
                print("IMPAR POSITIVO")
            else:
                print("NULO")

    except ValueError:
        print("Valor indefinido, digite um número inteiro")
leitor()