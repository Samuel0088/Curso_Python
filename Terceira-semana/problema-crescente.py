#Problema zeercicios "crescente"

def crescente():
    x = 0
    y = 1
    while (x != y):
        try:
            x = int(input("Digite dois números inteiros: "))
            y = int(input("Digite dois números inteiros: "))
            if (x < y):
                print("Os números estão emordem crescente.")
            elif (x > y):
                print("Os números estão em ordem decrescente.")
            else:
                print("Os números são iguais.")
        except ValueError:
            print("Valor inválido.")
    
crescente()