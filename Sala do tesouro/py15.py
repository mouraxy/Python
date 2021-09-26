#As variáveis do tipo float (%f)
#Valores reais (decimais, frações etc...)

valorDecimal1 = 3.14
valorDecimal2 = 3/4

#Exemplo de um programa para calcular a média (utilizando-se valores decimais/float e a estrutura "for" vista anteriormente):
contador = 0
nota = 0.0

qtdeNotas = int(input("\nQuantos valores você deseja inserir? "))
print("\n")

for contador in range(1, qtdeNotas + 1):
    print("Prova", contador)
    nota += float(input("Nota:"))

media = nota/qtdeNotas

#O %.(valor)f define o número de casas decimais depois da vírgula
print("\nSua média final é: %.2f\n" %media)






