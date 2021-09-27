#Números pseudo aleatórios: módulo random
#Pseudo porque não existe um método 100% eficiente para escolher um número aleatório (existem algoritmos para selecionar algum valor)

#Importando a biblioteca random
import random

#randrange: retorna aleatóriamente um elemento do range - (começo, fim, passo)
random.randrange(1, 7, 1)

#randint: retorna um inteiro N de tal forma que a <= N <= b - (a, b)
random.randint(1, 6)

#choice: retorna um elemento aleatório de uma sequência não-vazia (se não tiver valores, devolve um erro do tipo "IndexError")
random.choice([1, 2, 3, 4, 5, 6])

#random: retorna um número real entre 0.0 e 1.0
x = random.random()

#uniform: retorna um número real N de tal forma que a <= N <= b ou b <= N <= a - (a, b)
print(random.uniform(1, 7))
print(random.uniform(7, 1))