def tabuada():
    n = int(input("Deseja a tabuada para qual valor: "))
    try:
        for i in range(1, 11):
            print(f"A tabuada de {n} é: {n * i}")
    except ValueError:
        print("Entrada inválida")

tabuada()