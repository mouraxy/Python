#Exceções: introdução
#Erros levantados pelo Python (interrompem a execução)

#Bloco (try/except) 
#Tente o código:
try:
    Erro = input("Digite um valor inteiro: ")
    int(Erro)

#Ocorreu algum erro?
except:
    print("Ocorreu um erro!")

#Sempre vai executar (independente se deu erro ou não)
finally:
    print("Obrigado por digitar :)")

#A execução não é interrompida:
print("Continuando a execução...")