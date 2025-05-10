import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

def sortear():
    jogar_novamente = "y" #Iniciando o programa com a primeira inicialização verdadeira
    while jogar_novamente == "y": #Pegando a variavel e vendo se está igual os resultados atribuidos
        try:
            resultado = random.randint(1, 10) #Armazenando um numero de 1 a 10 em resultado
            numero = int(entrada_numero.get()) #Pedindo um numero ao usuario
            tentativas = 0 #Incrementando o numero de tentativas

            while True:
                    tentativas += 1 #Somando o numero de tentativas a cada loop rodado
                    if numero < resultado: 
                        numero = int(input("Muito baixo! Tente novamente: "))
                    elif numero > resultado:
                        numero = int(input("Muito alto! Tente novamente: "))
                    elif tentativas == 1:
                        print(f"Parabéns você acertou em uma tentativa! O número sorteado era {resultado}!")
                        break
                    else:
                        print(f"Parabéns você acertou em {tentativas} tentativas! O número sorteado era {resultado}!")
                        break

                    messagebox.showinfo("Resultado", resultado)
                    
            jogar_novamente = str(jogar_novamente.get()) #Pergutna ao usuario se quer jogar novamente
            if jogar_novamente != "y": #Se a resposta for diferente de y ele encerra o programa
                print("Obrigado por jogar, até a próxima!")

        except ValueError:
            messagebox.showerror("Erro, Por favor insira valores válidos")
            
#Configuração da janela
janela = tk.Tk()
janela.title("Projeto em Python")
janela.geometry("400x200")
janela.resizable(False, False)

#Labels e entrada
rotuloNumero = tk.Label(janela, text="Digite um numero de 1 a 10:")
rotuloNumero.grid(row=0, column=0, padx=10, pady=10)
entrada_numero = tk.Entry(janela)
entrada_numero.grid(row=0, column=1, padx=10, pady=10)
