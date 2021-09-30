#Detalhes sobre funções (nomenclatura e descrição)

#Não é considerada uma boa prática de programação colocar os nomes das variáves de forma semelhante ao nome da função (pode confundir)
def função():
    função = "Não é uma boa prática"

#Quando uma função é criada, aloca-se a mesma em um endereço de memória:
print(função)

#Você pode perder uma função se acabar definindo uma variável com o nome da mesma:
função = "Deixando de ser uma função"

#Descrição de uma função: é uma ótima prática para descrever o que uma função faz:
def Descrição(ops):
    """Isso é 
    um exemplo de 
    descrição"""

#Para ativar esse recurso, utiliza-se """ texto qualquer """ para definir a descrição e help(nomeDaFunção) para exibir tal recurso
help(Descrição)