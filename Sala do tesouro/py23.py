#Introdução à funções

#Criação: def declara que uma função será construída 
#Entre (): argumentos da função - valores que a função pode receber
#Return: indica o fim da função e o que será retornado
def nomeDaFunção(arg1, arg2):
    print("Executa algo...")
    return 

#Exemplos...
#1. Escreva uma função de potenciação:
def potenciação(base, expoente):
    pot = base**expoente
    return pot

#Passando os valores que serão utilizados nos argumentos da função:
resultado = potenciação(2, 3)
print("Resultado da potenciação: %i" %resultado)


#2. Faça uma função que necessite de três argumentos, e forneça a soma dos mesmos:
def soma(valor1, valor2, valor3):
    #Pode-se retornar uma expressão (perceba a diferença com o exercício anterior)
    return valor1 + valor2 + valor3

#Passando os 3 valores que serão utilizados nos argumentos da função:
resultadoSoma = soma(1, 2, 3)
print("Resultado da soma: %i" %resultadoSoma)


#3. Escreva uma função que recebe dois números e devolve a soma e a multiplicação entre eles:
def somaMultiplicação(valor1, valor2):
    #Pode-se retornar mais de um valor/expressão
    return valor1 + valor2, valor1 * valor2

#Definindo variáveis com mais de um retorno da função (primeiro é devolvido a soma e depois a multiplicação, a ordem importa!)
soma, multiplicação = somaMultiplicação(1, 2)
print(soma)
print(multiplicação)


#4. Crie uma função que sorteie um lançamento de dado e imprima o resultado:
import random

#Em algumas funções, não é necessário inserir argumentos (tudo é executado dentro da própria função)
def sorteioDado():
    resultadoSorteio = random.randint(1, 6)
    print("O valor do dado foi: %i" %resultadoSorteio)

#Chamando/executando função sem parâmetro/argumento
sorteioDado()