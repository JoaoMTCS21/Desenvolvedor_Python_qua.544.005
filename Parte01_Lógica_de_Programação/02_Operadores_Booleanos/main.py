# Declaração de variáveis
nome = input ("Informe seu nome: ") .strip () .title()
idade = int (input("Informe sua idade: "))
altura = float (input ("Informe sua altura em metros: ") .replace (",","."))

# Verifica se o pagante tem os requisitos.
if idade >= 12 and altura >= 1.35:
    print (f"{nome} está autorizado a entrar.")
else:
    print (f"{nome} não está autorizado a entrar.")