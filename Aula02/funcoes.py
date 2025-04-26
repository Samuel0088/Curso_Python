#Funções devem sempre vir no começo do código

# Problema "lanchonete" de zeercicios 2
#Função para calcular a quantidade a pagar e apresentar o valor na saída de dados

#Entrada de dados
def valor(a):
    return print(f"Valor a pagar = R$ {quantidade * a:.2f}")
try:
    print("| Código do produto | Preço do produto |")
    print("|          1        |       R$ 5.00    |")
    print("|          2        |       R$ 3.50    |")
    print("|          3        |       R$ 4.80    |")
    print("|          4        |       R$ 8.90    |")
    print("|          5        |       R$ 7.32    |\n")
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade de produto: "))
    valor_a_pagar = 0
    #Estrutura de controle de seleção MATCH CASE
    match codigo:
        case 1:
            valor(5.00)
        case 2:
            valor(3.50)
        case 3:
            valor(4.80)
        case 4:
            valor(8.90)
        case 5:
            valor(7.32)
except ValueError:
    print("Código inválido, tente novamente!")

