#Problema "negativos" zexercicios
def negativos():
    lista = []
    n = int(input("Quantos números você vai digitar: "))
    try:
        if (n <= 10):
            #Lê os números
            for i in range(n):
                x = int(input("Digite um número: "))
                lista.append(x)
            for i in range(n):
                if (lista[i] < 0):
                    print("Números negativos: ")
                    break
                else:
                    print("Não há números negativos na lista")
                    break
            for i in range(len(lista)):
                if (lista[i] < 0):
                    print(lista[i])
        else:
            #Não lê os números
            print("Excedeu o valor estimado!")
        
    except:
        print("Valor inválido, tente novamente!")
    
negativos()