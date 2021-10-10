#Formatações da função print e input
Dia = 18
Mes = 7
Ano = 2001
Decimal = 3.1415

#Função print normal:
print("\nData de nascimento do Felipe: ", Dia,"/", Mes,"/", Ano)

#Utilizando-se agora dos {} e do f antes das aspas:
print(f"Data de nascimento do Felipe: {Dia}/{Mes}/{Ano}")

#Definindo as casas decimais com o {:.númeroDeCasasDecimaisf}
print(f"O valor de PI é: {Decimal:.2f}")

#Para evitar quebras de linha utiliza-se (end = "separador"):
print("Evitando quebra de linha", end = " ")
print("com o o end!\n")

#Função input com os {} e o f antes das aspas:
input(f"De acordo com o algoritmo, você faz aniversário no dia {Dia}. Pode confirmar o valor? ")

#Método type(variável): retorna o tipo do dado
type(Dia)

#Pesquisar sobre os métodos is() --> É alguma coisa??