#Atividade 1

# Problema "terreno"
# Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
# casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
# o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
# duas casas decimais, conforme exemplo.
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
metro_quadrado = float(input("Digite o valor do metro quadrado: "))
area = largura * comprimento
preco = metro_quadrado * area
print(f"Area do terreno: {area}")
print(f"Preço do terreno: {preco}")


#Atividade 2
# Problema "retangulo"
# Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
# da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.
try:
    base = float(input("Base do retângulo: "))
    altura = float(input("Altura do retângulo: "))
    area = base * altura
    perimetro = base * 2 + altura * 2
    diagonal = ((base ** 2) + (altura ** 2)) ** 0.5
    print(f"Area = {area:.4f}")
    print(f"Perimetro = {perimetro:.4f}")
    print(f"Diagonal = {diagonal:.4f}")
except:
    print("Valor inválido, tente novamente!")