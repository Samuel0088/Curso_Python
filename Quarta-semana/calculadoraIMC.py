import tkinter as tk
from tkinter import *
from tkinter import messagebox

def calcular_imc():
    try:
        #Entrada de dados
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        #Processamento de dados
        imc = peso / (altura ** 2)
        #Variavel para guardar o dado do imc formatado
        resultado = f"Seu IMC é: {imc:.2f}\n"

        #Classificação do IMC   
        if imc < 18.5:
            resultado += "Classificação: Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            resultado += "Classificação: Peso normal"
        elif 25 <= imc < 29.9:
            resultado += "Classificação: Sobrepeso"
        else:
            resultado += "Classificação: Obesidade"

        messagebox.showinfo("Resultado", resultado)
    except:
        messagebox.showerror("Erro, Por favor insira valores válidos")

#Configuração da janela
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("400x200")
janela.resizable(False, False)

#Labels e entrada
rotuloPeso = tk.Label(janela, text="Peso(kg):")
rotuloPeso.grid(row=0, column=0, padx=10, pady=10)
entrada_peso = tk.Entry(janela)
entrada_peso.grid(row=0, column=1, padx=10, pady=10)

rotuloAltura = tk.Label(janela, text="Altura(cm): ")
rotuloAltura.grid(row=1, column=0, padx=10, pady=10)
entrada_altura = tk.Entry(janela)
entrada_altura.grid(row=1, column=1, padx=10, pady=10)

#Botao para calcular o IMC
btn = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
btn.grid(row=2, column=0, columnspan=2, pady=20)

#Inciar o loop da interface gráfica
janela.mainloop()