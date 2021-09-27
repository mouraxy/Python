#Atalhos e formatações da função print e input (maior legibilidade)
Dia = 18
Mes = 7
Ano = 2001

#Para inteiros --> %i ou %d
#Para floats (números decimais) --> %f
#Para strings (textos) --> %s

#print
print("Data de nascimento do Felipe: ", Dia,"/", Mes,"/", Ano)

#Mesmo resultado, utilizando-se agora o % na função print (formato da variável)
print("Data de nascimento do Felipe: %i/%i/%i" %(Dia, Mes, Ano))

#input 
input("De acordo com o algoritmo, você faz aniversário no dia %i. Pode confirmar o valor? " %Dia)