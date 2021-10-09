#Elif (senão se)
idade = int(input("Digite sua idade: "))

#Criação do mesmo código anterior (utilizando-se desta vez o elif):
if 18 <= idade < 60:
    print("Você é adulto :(")
elif idade < 18: 
    print("Você é jovem :)")
else: 
    print("Você é idoso :)")

#Deste modo, todas as faixas etárias estão sendo referenciadas