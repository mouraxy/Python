#Atalhos e formatações da função print e input (maior legibilidade)
Dia = 18
Mes = 7
Ano = 2001
Decimal = 3.1415

#Para inteiros --> %i ou %d
#Para floats (números decimais) --> %f
#Para strings (textos) --> %s

#Função print e seus detalhamentos:
#print normal
print("Data de nascimento do Felipe: ", Dia,"/", Mes,"/", Ano)

#Mesmo resultado, utilizando-se agora o % na função print (formato da variável)
print("Data de nascimento do Felipe: %i/%i/%i" %(Dia, Mes, Ano))

#Mesmo resultado, porém utilizando agora as {} e o .format(variáveis)
print("Data de nascimento do Felipe: {}/{}/{}" .format(Dia, Mes, Ano))

#O %.(valor)f define o número de casas decimais depois da vírgula
print("\nSua média final é: %.2f" %Decimal)

#Definição das casas decimais, agora com o {:.númeroDeCasasDecimaisf}
print("\nSua média final é: {:.2f}" .format(Decimal))

#Para evitar quebra de linha, utiliza-se (, end = " ")
print("Evitando quebra de linha", end = " ")


#Função input e seus detalhamentos:
#input utilizando o %
input("De acordo com o algoritmo, você faz aniversário no dia %i. Pode confirmar o valor? " %Dia)

#input utilizando as {} e o .format(variável)
input("De acordo com o algoritmo, você faz aniversário no dia {}. Pode confirmar o valor? " .format(Dia))


#Métodos: 
#type(variável): retorna o tipo do dado
type(Dia)

#variável.is____(): tem várias opções e retorna diversas informações de testagem ("é alguma coisa?")