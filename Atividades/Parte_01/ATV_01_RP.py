#TODO - Atividade - 01 - Respondida pelo professor
'''
Crie um programa que receba o nome, a massa em kg e a altura em metros do usuário, calcule seu IMC (Índice de massa corporal) e finalize informando o diagnóstico do usuário com base no valor do IMC (se está magro, gordo ou no peso ideal...)
'''

# Entrada de Dados

nome = input ("Informe seu nome: ") .strip () .title()
massa = float (input ("Informe sua massa em kg: ") .replace ("," , "."))
altura = float (input ("Informe sua altura em metros: ") .replace ("," , "."))

# Calcular o IMC

imc = massa / (altura ** 2)

# Exibe o valor do IMC

print (f"{nome}, seu IMC é {imc:.2f} !")

# Informe o diagnóstico

if imc < 18.5:
    print ("Você está abaixo do peso ideal.")

elif imc < 25:
    print ("Você está no peso normal. ")

elif imc < 30:
    print ("Você está com massa acima do normal. ")

elif imc < 35:
    print ("Você está obeso. ")

elif imc < 40:
    print ("Você está com obesidade nível II")

else:
    print ("Você está com obesidade mórbida.")

# (Observação !) Utilizar o operador "and" não possui uma finalidade aqui, pois para cair em uma dessas opções, automaticamente já passa pelas outras. Além do operador "and" ser mais pesado para a memória.