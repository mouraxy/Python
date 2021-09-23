#Variável booleana

#Variáveis Booleanas
#Derivando do tipo inteiro, possuem dois valores constantes: True e False (verdadeiro e falso)
#Utilizados como verificação

#Neste caso, o Python devolverá o valor da variável booleana como "True"
VerdadeiroOuFalso = 14<15
print(VerdadeiroOuFalso)

#Neste caso, o Python devolverá o valor da variável booleana como "False"
VerdadeiroOuFalso = 15<14
print(VerdadeiroOuFalso)

#Mais um algoritmo com sua utilização:
#Você pode consumir bebida alcólica (verdadeiro ou falso)?
idade = int(input("Digite sua idade: "))
podeBeber = idade >= 18
print(podeBeber)

#O computador é construído para interpretar valores binários (0,1) 
#True == 1 significa que está passando corrente
#False == 0 significa que a corrente foi cortada
True == 1
False == 0

#Método de construção (função) bool transforma algum valor para "True"
converteValor = bool(10)
print(converteValor)
