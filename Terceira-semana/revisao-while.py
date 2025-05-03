#Estrutura de controle enquanto (while)

try:
    i = int(input("Digite o valor inicial de i: "))
    while (i < 10):
        print("Estou dentro do loop", i)
        i += 1
except:
    print("Informações erradas")