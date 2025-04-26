#Aluno: Samuel Vieira
try:
    n1 = int(input("Primeiro valor: "))
    n2 = int(input("Segundo valor: "))
    n3 = int(input("Terceiro valor: "))

    if n1 < n2 and n3:
        print(f"Menor: {n1}")
    elif n2 < n1 and n3:
        print(f"Menor: {n2}")
    elif n3 < n2 and n1:
        print(f"Menor: {n3}")
    else:
        print(f"Menor: {n1}")
except:
    print("Digite um número inteiro")