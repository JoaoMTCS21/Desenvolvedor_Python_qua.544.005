# Declaração de Variáveis
nome = input ("Informe seu nome: ") .strip ().title ()
idade = int (input ("Informe sua idade: "))

# Operador Ternário = Simplificação estrutural de um if else.

print (f"{nome} {'É maior de idade' if idade >=18 else 'É menor de idade'}.")