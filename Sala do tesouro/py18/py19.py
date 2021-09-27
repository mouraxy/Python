#Continuação listas

#É possível inserir listas dentro de outras listas:
lista  =  [1, 2, 3, [4, 5, 6]]
#Índices:  0  1  2      3

#Obtendo-se o elemento de uma lista dentro de outra lista:
#Índice da lista inserida na outra lista [3]
#Índice do elemento na lista inserida na outra lista [0]
print(lista [3][0])

#Adicionando novos elementos através do método append
lista = []

for i in range (1, 6):
    valor = int(input("Digite o %i número da lista: " %i))
    lista.append(valor)

print(lista)

#Outro ponto importante é que listas (vetores) armazenam endereços na memória