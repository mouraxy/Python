#Arquivos: modos de abertura e métodos

#Modos de abertura:
#"w" --> write (escrever)           
#"r" --> read (ler)           
#"a" --> append (adicionar)


#Criando um arquivo txt:
#                nome do arquivo, modo de escrita
arquivoEscrita = open("Olá arquivo.txt", "w")

#Método write(string): insere caracteres dentro do arquivo criado
arquivoEscrita.write("Inserindo palavras no arquivo\n")
arquivoEscrita.write("Inserindo mais palavras no arquivo\n")

#Método writelines(): recebe uma lista de strings
arquivoEscrita.writelines(["Inserindo ", "palavras"])

#Fechando o arquivo (sempre é necessário):
arquivoEscrita.close()

#                nome do arquivo, modo de leitura
arquivoLeitura = open("Olá arquivo.txt", "r")

#Método read(): retorna todos elementos do arquivo em uma única string
print(arquivoLeitura.read())

#Método readlines(): retorna todos elementos do arquivo, colocando cada linha em um índice de uma lista
#print(arquivoLeitura.readlines())

#O Python relembra o local em que ele parou de ler!

#Fechando o arquivo (sempre é necessário):
arquivoEscrita.close()


#                nome do arquivo, modo de adicionar
arquivoAdicionar = open("Olá arquivo.txt", "a")
arquivoAdicionar.write("\nAdicionando mais elementos em um arquivo criado anteriormente!")