#Atividade 03
def atividade03():
    x = 1
    soma = 0
    while (x != 0):
        try:
            x = int(input("Digite o valor inteiro: "))
            if x%2 == 0:
                soma = x + (x + 2) + (x + 4) + (x + 6) + (x + 8)
                print("soma = ", soma)
            elif (x%2 != 0):
                x += 1
                soma = x + (x + 2) + (x + 4) + (x + 6) + (x + 8)
                print("Soma = ", soma)
        except:
            print("Valor inválido, tente novamente!")

atividade03()