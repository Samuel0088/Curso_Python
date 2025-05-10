import random #Importa a biblioteca para sortear os números de 1 a 10

print("====  Jogo de adivinhar número  ====") #Enfeite no topo do código

jogar_novamente = "y" #Iniciando o programa com a primeira inicialização verdadeira ou seja y
while jogar_novamente == "y": #Pegando a variavel e vendo se está igual ao resultado atribuido no while
    try:
        resultado = random.randint(1, 10) #Armazenando um numero de 1 a 10 em resultado
        numero = int(input("Informe um número aleatório (1 a 10): ")) #Pedindo um numero ao usuario
        tentativas = 0 #iniciando a variavel que ira incrementar o numero de tentativas

        while True: #Enquanto for verdadeiro
                tentativas += 1 #Somando o numero de tentativas a cada loop rodado
                if numero < resultado:  #se o numero digitado pelo usuario for menor que o numero sorteado
                    numero = int(input("Muito baixo! Tente novamente: "))
                elif numero > resultado:#se o numero digitado pelo usuario for maior que o numero sorteado
                    numero = int(input("Muito alto! Tente novamente: "))
                elif tentativas == 1:#se o numero digitado pelo usuario for igual que o numero sorteado no entanto o usuario acertou em uma unica chance
                    print(f"Parabéns você acertou em uma tentativa! O número sorteado era {resultado}!")
                    break
                else: #se o numero digitado pelo usuario for igual que o numero sorteado
                    print(f"Parabéns você acertou em {tentativas} tentativas! O número sorteado era {resultado}!")
                    break

        jogar_novamente = input("Deseja jogar novamente? (y/n): ") #Pergunta ao usuario se quer jogar novamente
        if jogar_novamente != "y": #Se a resposta for diferente de y ele encerra o programa
            print("Obrigado por jogar, até a próxima!")

    except ValueError:#Tratamento de erro caso o usuario nao digite um numero
        print("Valor incorreto, tente novamente!")
        