try:   
    #Calculadora
    valor1 = float(input("Digite um valor: "))
    valor2 = float(input("Digite outro valor: "))
    #--------------------------------------------#
    print("Selecione a operação desejada:")
    print("1- Soma\n2- Subtração \n3- Multiplicação \n4- Divisão \n5- Exponenciação")
    opcao = input("Digite o valor desejado: ")
    #-- Estrutura de controle de decisão IF ELIF ELSE --#
    if opcao == "1":
        print("A soma dos valores é: ", valor1 + valor2)
    elif opcao == "2":
        print("A subtração dos valores é: ", valor1 - valor2)
    elif opcao == "3":
        print("A multiplicação dos valores é: ", valor1 * valor2)
    elif opcao == "4":
        if valor2 != 0:
            print("A divisão dos valores é: ", valor1 / valor2)
        else:
            print("Divisão impossível")
    elif opcao == "5":
        print("A exponenciação dos valores é: ", valor1 ** valor2) 
    else:
        print("Opção não encontrada, tente novamente!")
except ZeroDivisionError:
    print("Divisão impossível")
except ValueError:
    print("Valor invalido")