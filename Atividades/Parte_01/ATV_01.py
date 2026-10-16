#TODO - Atividade - 01
'''
Crie um programa que receba o nome, a massa em kg e a altura em metros do usuário, calcule seu IMC (Índice de massa corporal) e finalize informando o diagnóstico do usuário com base no valor do IMC (se está magro, gordo ou no peso ideal...)
'''

import os

os.system ("cls" if os.name == "nt" else "clear")

nome = input ("Digite o nome do paciente: ") .strip () .title ()
altura = float ( input ("Digite a altura do paciente em metros: ") .replace ("," , "."))
massa = float ( input ("Digite a massa do paciente KG: ") .replace ("," , "."))
imc = massa / (altura * altura)

if imc <= 18.5:
 print (f"O paciente {nome} possui um imc de {imc:.2f}, o que indica um peso abaixo do ideal.")

elif imc <= 18.6 and imc <= 24.9:
 print (f"O paciente {nome} possui um imc de {imc:.2f}, o que indica um peso ideal.")

elif imc <= 25.0 and imc <= 29.9:
 print (f"O paciente {nome} possui um imc de {imc:.2f}, o que indica que está acima do peso ideal.")

else:
 print ("O cálculo do imc não pode ser feito corretamente. ")