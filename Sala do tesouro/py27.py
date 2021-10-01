#Statements: Break e Continue
#São utilizados em ciclos de repetição (while e for)

#Break ---> parar ou interromper
for i in range(10):
    if i == 5: 
        #Interrompe o loop (for/while) em que está contido
        print("Parando...")
        break
    print(i)

#Continue --> Reenicia o ciclo for/while (retorna para o começo do ciclo em que está contido, desconsiderando o que estava abaixo na respectiva repetição)
for i in range(10):
    if i == 5:
        print("Voltando para o começo...")
        continue
    print(i)

#Outro exemplo de "continue":
lista = [1, 2, 3, 4, 5, 6]
impar = []

#A lista será integralmente percorrida...
for i in lista:
    if i % 2 == 0:
        #Neste caso, se o elemento da lista for divisível por 0 ele retorna para o início do ciclo
        continue
    #Caso não seja, ele é considerado ímpar e adiciona-se o elemento na lista destinada para tais valores
    impar.append(i)

print(impar)