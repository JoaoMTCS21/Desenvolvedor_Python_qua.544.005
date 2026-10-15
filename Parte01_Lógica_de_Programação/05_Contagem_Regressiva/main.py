# Importa as bibliotecas

import os
import time

# Limpa Terminal
os.system("cls")

# Entrada de Dados

n = int ( input ("Informe um Número Inteiro: "))

#Contador
while n >= 0:
    os.system ("cls")
    print (f"{n}...")
    time.sleep (1)
    n -= 1
print ("BOOM !!!")