# Bibliotecas

import os

# Lista Vazia

tarefas = []

# Limpa Terminal

os.system ("cls" if os.name == "nt" else "clear")

# Loop

while True:
    # Menu

    print ("1 - Inserir nova tarefa na lista")
    print ("2 - Finalizar e exibir a lista")
    opcao = input ("Opção desejada: ") .strip () # Informa a opção desejada

    # Verifica a opção desejada

    match opcao:
        case "1":
         nova_tarefa = input ("Informe a nova tarefa: ") # Usuário informa um novo item
         tarefas.append (nova_tarefa) # Insere um item a lista
         continue # Retorna ao início do loop

        case "2":
         os.system ("cls" if os.name == "nt" else "clear")

         # Exibe a lista 
         for n, tarefa in enumerate (tarefas, start = 1):
             print (f"{n}ª tarefa: {tarefa}")
         break # Encerra o loop
        
        case _:
          print ("Opção inválida.")

pass