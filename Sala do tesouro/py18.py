#Introdução à listas
#Armazena um conjunto de valores (com quaisquer formatos)

#Criação: nome da variável = [valores]
lista  =  [1, 2, 3 ,4]
#Índices:  0  1  2  3
#Índices: -4 -3 -2 -1

#Acessando um desterminado elemento da lista (a contagem de uma lista (índices) começa a partir de 0):
print(lista[3])

#É possível colocar índices negativos (será contado ao contrário):
print(lista[-1])

#Adicionando elementos em uma lista (lista += [novo elemento a ser adicionado]):
#Neste caso, o novo valor inserido é movido para o final da lista
lista += [5]

#Operações matemáticas entre elementos pertecentes a uma mesma lista:
lista[3] + lista [3]
lista[3] - lista [3]
lista[3] * lista [3]
lista[3] / lista [3]
lista[3] ** lista [3]

#Como mudar os elementos de uma lista?
#Nome da lista[posição do elemento que será trocado] = novo valor
lista[0] = 4.4

#Pode-se criar listas a partir de variáveis
a = 1
b = 2
c = 3
d = int(input("Insira um valor na lista: "))

listaVariaveis = [a, b, c, d]

#Slice percorre a lista e constrói uma sublista a partir dos valores obtidos - (de tal elemento : a tal elemento): 
lista[1 : 3]

#Duplo slice (o terceiro parâmetro é o passo/pulo do índice)
lista[0 : 5 : 2]
