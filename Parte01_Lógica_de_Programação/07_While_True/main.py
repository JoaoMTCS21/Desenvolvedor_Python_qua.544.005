#Importa uma biblioteca

import os

# Limpa a tela

os.system ("cls" if os.name == "nt" else "clear")

# Loop

while True: 
    aluno = input ("Informe o nome do aluno: ") .strip () .title ()

    try:
       nota = float ( input ("Informe a nota de 0 a 10 do aluno: .") .replace (",","."))

       if nota >= 0 and nota <= 10:
            
            if nota >= 7:
               
               print (f"{aluno} está aprovado.")

            elif nota >= 5:
               
               print (f"{aluno} está de recuperação.")
            else:
               
               print (f"{aluno} está reprovado.")
       else:

        print ("Nota inválida.")

    except Exception as e:

        print (f"Não foi possível calcular a média. {e}.")

    continuar = input ("Deseja continuar a inserir as informações ?.'sim' para prosseguir. Qualque outro valor será considerado como 'não' ") .strip () .lower()

    if continuar == "sim":
        os.system ("cls" if os.name == "nt" else "clear")
        continue
    else:
        break