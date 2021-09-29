#Estrutura condicional: if e else
idade = int(input("Digite sua idade: "))

#Criando estrutura condicional:
if idade >= 18:
    print("Pode entrar na festa...")
    #Você pode inserir blocos comparativos dentro de outras estruturas comparativas
    if idade > 40:
        print("Mas está ficando velhinho para isso")
else:
    print("Não pode entrar na festa...")

#De modo comparativo o if tem o significado de "se"
#Por sua vez, o else tem o significado de "senão"