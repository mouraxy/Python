#Listas: função list e métodos pop, index, insert, sort, copy e clear 
lista = [1, 2, 3, 4, 1, 2, 3, 4]

#Função list: transforma valores específicos em uma lista (só funciona com os tipos abaixo)

#1. Textos são armazenados na lista em caracteres
list("Olá, tudo bem?")
#2. Range(valor mínimo, valor máximo)
list(range(1, 10))

#Pop: remove um determinado elemento pelo seu índice, e posteriormente devolve o valor excluído - (índice)
lista.pop(0)

#Index: mostra o primeiro índice que contém um determinado valor - (valor a ser procurado)
lista.index(3)

#Insert: insere algum elemento em uma determinada posição da lista - (index, valor)
lista.insert(1, 0)

#Sort: organiza os elementos de uma lista em ordem crescente
lista.sort()

#Copy: copia todos os elementos de uma lista e os transfere (o recebedor é totalmente independente)
copia = lista.copy()

#Clear: remove todos os elementos de uma lista
lista.clear()