# Declaração de Variáveis

x = float ( input ("Informe um Número: ") .replace (",", "."))
y = float ( input ("Informe um Outro Número: ") .replace (",","."))
operador = input ("Operação Desejada: ") .strip()

# Match_Case
match operador:
    case "1":
        print (f"Resultado da Soma: {x+y}")
    case "2":
        print (f"Resultado da Subtração: {x-y}")
    case "3":
        print (f"Resultado da Multiplicação: {x*y}")
    case "4":
        print (f"Resultado da Divisão {x/y}")
    case _:
        print ("Operação Inválida ")