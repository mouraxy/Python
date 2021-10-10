#Módulo sys
import sys

#Sys.platform: demonstra a plataforma de execução
print(sys.platform)

if 'win' in sys.platform:
    print("Essa é uma plataforma Windows!")

#Sys.exit: encerra todos os scripts em Python.
sys.exit()