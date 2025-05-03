lista = []
def negativos():
    n = int(input("Quanto números vc vai digitar? "))
    try:
        if (n<=10):
            #Lê os números
            for i in range(n):
                x = int(input("Digite um número: "))
                lista.append(x)
            for i in range(n):
                if (lista[i]<0):                      
                    print("Números negativos: ")
                    break
                else:
                    print("Não há números negativos na lista")
                    break
            for i in range(len(lista)):
                if (lista[i]<0):
                    print(lista[i])
        else:
            #Não Lê os números
            print("Excedeu o valor estimado!")
    except:
        print("Valor invalido tente novamente!")
def soma():
    soma = 0
    for i in range (len(lista)):
        soma += lista[i]
    print("Soma  = ", soma)
    return soma

negativos()
print(lista)      
soma = soma()
print(soma)
media = soma/(len(lista))
print("Media = ", media)