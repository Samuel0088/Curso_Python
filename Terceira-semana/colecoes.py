#Coleções em python
#Lista = [] -> lista = ["senai", True, 22, 3.5]
#Tupla = () -> tupla = ("senai", True, 22, 3.5)
#Dicionário = {} -> dicionario = {"nome": "senai", "logica": True}
#Conjuntos = {} -> conjunto = {"senai", True, 10, 1.75}

#Definições
#Lista: É uma coleção ordenada e mutavel. Permite membros duplicados

#Tuplas: É uma coleção ordenada e imutável. Permite membros duplicados

#Dicionário: É uma coleção ordenada e mutável. Nenhum membro duplicado

#Conjunto: É um coleção não ordenada e não indexada. Nenhum membro duplicado

#-------------------------Lista-----------------------#
#a lista é acessada por indices
lista = ["Senai", True, 22, 3.5]
print(len(lista)) #tamanho da lista
print(type(lista)) #tipo da lista
del lista[1] #apagar um elemento da lista
lista.append("Feriado") #insere um elemento na lista
lista.insert(0, "Clodoaldo") #insere um elemento na lista
print(lista)

#-------------------------Tupla-----------------------#
tupla = ("Senai", True, 22, 1.73)
print(tupla)
print(tupla[3])

#-------------------------Dicionário-----------------------#
#Não é acessado por indices e sim palavras chaves
dicionario = {"nome": "Senai", "Lógica": True, "numero": 2, "num": 1.5}
print(dicionario["nome"])
for i in dicionario.keys():
    print(i, "->", dicionario[i])
dicionario.update({"novo": "Samuel"}) #Adiciona itens em um dicionario
del dicionario["Lógica"]
print(dicionario)

#-------------------------Conjunto-----------------------#
conjunto = {"senai", True, 10, 1.75}
print(type(conjunto))

