#Módulos 
#São um conjunto de códigos-fonte externos que podemos importar em nossos scripts

#Importando o módulo math (com todas suas funcionalidades matemáticas)
import math

#Nome do módulo.comando desejado

#Seno
math.sin(30)

#Cosseno
math.cos(30)

#Tangente
math.tan(30)

#Potenciação (primeiro número elevado ao segundo número)
math.pow(2, 2)

#Raíz quadrada
math.sqrt(4)

#Número de pi
math.pi

#Para importar um único comando de um módulo utiliza-se:
#from módulo import comando
from math import sin

#Porém, agora não é mais preciso inserir o nome do módulo na frente do comando
sin(30)

#Pode-se também, alterar o nome do módulo (modificando a forma em que ele é escrito no código):
import math as matematica

matematica.sin(30)

#Bem como, alterar o nome do comando:
from math import sin as seno

seno(30)