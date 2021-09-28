#Continuação de funções

#Argumentos variáveis: não se sabe a quantidade exata de argumentos passados para a função (utiliza-se *)
#O *, por sua vez, coloca todos os argumentos passados em uma sequência (tuplas), como se fosse um tipo de listas imutáveis

#Ressalta-se, que você pode ter os dois seguintes tipos de argumentos juntos no Python, porém, com a ordem sendo: argumentos definidos primeiro, *argumentos variáveis depois
def argumentosNãoDefinidos(num1, *valores):
    print(valores)

#O primeiro argumento assume o primeiro valor passado, o restante é imerso no argumento variável (como se fosse o resto não definido) 
                     #num1
argumentosNãoDefinidos(1, 2, 3, 4, "Olá, tudo bem?")
                          #------- *valores-------

#Desta forma, pode-se utilizar a quantidade de argumentos que desejar


#Argumentos pré definidos: é possível inserir valores para os argumentos (geralmente utilizado quando tem valores fixos):
#Sempre é colocado no final dos argumentos!
def inserindoValores (argumento1, argumento2 = 2, argumento3 = 3):
    print(argumento1, argumento2, argumento3)

#Desta forma, esconomiza-se a quantidade de argumentos que será necessário informar (já que alguns foram definidos anteriormente)...
inserindoValores(1)
            #argumento1