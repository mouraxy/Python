#Strings: padrão ASCII

#ASCII: código padrão americano para intercâmbio de informações
#Padroniza o conjunto de caracteres em lingugagem de máquina (binário)

#chr(valor inteiro): devolve o caractere correspondente ao número inteiro (ASCII)
for i in range(256):
    print("%.3i - %s"%(i, chr(i)))

#ord(caractere): devolve o número inteiro correspondente ao caractere (ASCII)
print(ord('a'))

#Letras maiúsculas se diferem das minúsculas:
print("A" != "a")