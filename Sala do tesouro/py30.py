#Strings: continuação...
#         0    1    2    3
lista = ["A", "B", "C", "D"]

#Imprimindo o primeiro valor da lista:
print(lista[0])

#Utilizando-se do split para strings:
print(lista[0:3])
print(lista[:3])
print(lista[0:])

#Com intervalos (terceiro parâmetro)
print(lista[0:4:2])
print(lista[0::2])


frase = "Esse é um exemplo de string."

#Método len(): retorna a quantidade de caracteres
print(len(frase))

#Método count(): retorna a quantidade de vezes que um caractere aparece
print(frase.count("A"))

#Operador in:
print("A" in frase)

#Método replace(valor antigo, valor novo): utilizado para substituir uma ou mais ocorrências de um determinado conteúdo em uma string
print(frase.replace('Esse', 'Trocou'))

#Método upper(): coloca os caracteres em letra maiúscula
print(frase.upper())

#Método upper(): coloca os caracteres em letra minúscula
print(frase.lower())

#Método capitalize(): coloca o primeiro caractere em letra maiúscula
print(frase.capitalize())

#Método title(): baseando-se nos espaços, coloca a primeira letra de cada palavra em maiúscula
print(frase.title())

#Método strip(): remove os espaços "inúteis" no início e fim do conjunto de caracteres
print(frase.strip())

#Método split(): divide uma sequência de caracteres baseando-se nos espaços (as divisões são inseridas em uma lista)
print(frase.split())

#Exercício de fixação:
#Quantas letras tem o seu nome? 
nome = input("\nDigite seu nome completo: ")
print("Seu nome tem {} letras" .format(len(nome) - nome.count(' ')))