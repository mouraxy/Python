#Módulo os
import os

#getpid(): ID do processo (PID):
print(os.getpid()) 
 
#getcwd(): diretório sendo utilizado:
print(os.getcwd())

#rename('nome antigo do arquivo.extensão', 'novo nome.extensão'): altera o nome de um determinado arquivo
try:
    nomeAntigo = input("Digite o nome do arquivo que deseja mudar: ")
    NovoNome = input("Digite o novo nome do arquivo: ")
    os.rename(nomeAntigo, NovoNome)
except:
    print("Não foi possível localizar :(")

#remove('nome do arquivo): revove um determinado arquivo permanentemente
try:
    os.remove(NovoNome)
    print(NovoNome, "foi excluído com sucesso!")
except:
    print("Não foi possível excluir o arquivo {}!" .format(NovoNome)) 

#urandom(bytes): devolve uma string criptografada e aleatória com um determinado tamanho em bytes
print(os.urandom(5))

#Apresentar o nome do usuário:
print(os.environ['USERNAME'])

#O módulo os.path possuí variadas características próprias envolvendo diretórios (pesquisar sobre)