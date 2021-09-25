#Variáveis
#São espaços na memória do computador destinado a um dado 

#Declaração 
#Nome da variável = valor da variável
Idade = 19 
Meses = 10

#Pode-se ser utilizada em diversas situações:
print("Eu tenho", Idade, "anos e", Meses, "meses")

#É possível atribuir a uma variável o valor de outra variável
Variavel1 = 1
Variavel2 = 2 
Variavel3 = 3 

#Neste caso o valor 1 se transformará em 2
Variavel1 = Variavel2 
print(Variavel1)

#Neste caso o valor 1 se transformará em 2, na qual, valerá 3 posteriormente 
Variavel1 = Variavel2 = Variavel3 
print(Variavel1)

#Outra forma de declarar uma variável em Python
Exemplo1, Exemplo2 = 1, 2

#Regras de declaração
#Não pode conter espaços 
Exemplo Errado = 1

#Não pode conter caracteres especiais
!@$%&*()[]/?,;-+= = 1

#Pode-se utilizar acentos no nome da variável
VariávelComAcento = 1

#Pode-se utilizar _ (underline) no nome da variável
Exemplo_com_Underline = 1