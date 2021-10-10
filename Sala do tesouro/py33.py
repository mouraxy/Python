#Módulo time
import time

#Função asctime(): retorna o dia da semana, mês, dia, horário e ano
print(time.asctime())

#Função localtime(): retorna todos os parâmetros de data e horário em uma tupla (podem ser acessados separadamente)
dataHorario = time.localtime()
mês = print(dataHorario[1], end="/")
ano = print(dataHorario[0])

#time(): utilizado para medir intervalos de tempo
t1 = time.time()

#Código
x = 0
while x < 1000000:
    x += 1

#Quanto tempo demorou a execução?
t2 = time.time()
print("{:.2f} segundos" .format(t2 - t1))

#Função sleep(): pausa a execução do programa em uma determinada quantidade de segundos
segundos = 10

for i in range(segundos):
    print("Contagem regressiva: {}" .format(segundos))
    segundos = segundos - 1
    time.sleep(1)

print("Fim da contagem!")