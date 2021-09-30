#Funções: Variáveis globais e locais
#O Python cria cópias das variáveis presentes em funções (independentes) com excessão das listas

#Váriaveis locais ficam restritas em uma parte específica do programa 
def função():
    VariavelLocal = "Isso é uma variável local contida exclusivamente dentro de uma função" 

#Não podem ser referenciadas em outras localidades (é como se não existissem)...
print(VariavelLocal)

#Variáveis globais necessitam ser criadas no script geral do programa, além serem criadas antes de sua utilização
VariávelGlobal = "Isso é uma variável global, ela pode ser utilizada em quaisquer localidades específicas de um algoritmo"

#Para utilizá-la, basta referenciar a mesma com "global":
def funçãoDois(): 
    global VariávelGlobal
    print(VariávelGlobal, " - Dentro da função") 

funçãoDois()
print(VariávelGlobal)