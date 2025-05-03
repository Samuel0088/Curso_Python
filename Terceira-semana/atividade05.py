#Aluno: Samuel Vieira
lista = []

def imprimir():
    try:
        n = int(input("Quantos numeros voce vai digitar: "))
        for i in range(n):  
            x = int(input("Digite um numero: "))
            lista.append(x)
        print("Lista digitada:", lista)
    except ValueError:
        print("Digite valores inteiros")

imprimir()

def pares():
    contador = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            print("Numeros pares:", lista[i])
            contador += 1
    print("Quantidade de numeros pares:", contador)

pares()
