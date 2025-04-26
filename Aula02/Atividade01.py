try:
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    pergunta1 = n1 == n3
    pergunta2 = n1 != n2
    pergunta3 = n2 > n1
    pergunta4 = n2 <= n3
    print("1- O primeiro valor é igual ao terceiro valor? R:", pergunta1)
    print("2- O primeiro valor é diferente do segundo valor? R:", pergunta2)
    print("3- O segundo valor é maior que primeiro valor? R:", pergunta3)
    print("4.O segundo valor é menor ou igual que terceiro valor? R:", pergunta4)

    print(pergunta1 == True and pergunta3 == True)
    print(pergunta2 == True or pergunta4 == True)
    print(not pergunta1)

except:
    print("Digite um número inteiro")