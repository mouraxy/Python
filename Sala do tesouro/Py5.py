#Função input
#Imprime uma mensagem na tela, e aguarda informações a serem digitadas pelo usuário
input("Digite alguma mensagem: ")

#Pode-se atribuir o valor digitado em uma variável, porém, o mesmo é salvo como uma string (formato de texto)
valorDigitado = input("Valor: ")

#Então, converte-se o valor textual para um número inteiro (caso necessário)
valorDigitado = int(valorDigitado)

#Ou como poderia ter sido usado desde o começo (para conseguir um valor inteiro)
valorDigitado = int(input("Valor: ")) 

