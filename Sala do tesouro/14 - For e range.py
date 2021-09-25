#Estruturas de repetição: for e range
n = 10

#O ciclo for é um ciclo que percorre uma determinada sequência e tem o significado de "para"
for contador in range(n):
    print (contador)

#Range cria uma sequência de números com determinadas condições
#Porém, você pode definir ou modificar tais atributos conforme a estrutura: range(valor inicial, final, distância entre os números/incrementador):
for contador in range(0, 10, 2):
    print ("Números pares até dez: ", contador)

#É possível criar uma sequência decrescente:
for contador in range(10, 0, -1):
    print ("Contagem regressiva: ", contador)



