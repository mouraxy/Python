#Listas: for, além dos métodos reverse e remove

#Utilização do for para listas
numeros = [1, 2, 3, 4, 5]

#Para i dentro de "numeros" (percorre a lista)
for i in numeros:
    print(i)

#Reverse: inverte os valores da lista 
lista = [1, 2, 3, [4, 5]]
lista.reverse()

#Remove: procura um determinado valor, e excluí ele da lista - (valor a ser retirado)
lista.remove(2)

#É possível retirar listas
lista.remove([4, 5])