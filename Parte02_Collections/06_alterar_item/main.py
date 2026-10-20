# Bibliotecas

import os

# Lista

nomes = ["Alex", "Charlotte", "Scarlet", "John", "Jason", "Michael", "Connor", "Robert"]

os.system ("cls" if os.name == "nt" else "clear")

# Loop

while True:

    # Exibe a lista original

    for n, nome in enumerate (nomes):
        print (f"Índice {n}: {nome}")

    #Menu
    print (" 1 - Alterar item da lista")
    print (" 2 - Finalizar")
    opcao = input (" Opcão desejada: ") .strip () # Informa a opção desejada

    # Verifica a opção escolhida

    match opcao:
        case "1":

            # Informa índice a ser alterado

            indice = int ( input ("Informe o índice a ser alterado: "))

            # Informa novo valor

            nomes [indice] = input (" Informe um novo nome: ") .strip() .title ()            
            os.system ("cls" if os.name == "nt" else "clear")
            print (" Item da lista alterado com sucesso!")
            continue

        case "2":
            os.system ("cls" if os.name == "nt" else "clear")

            # Exibe uma nova lista

            for n, nome in enumerate (nomes):
                print (f"Índice {n}: {nome}")
            break

        case _:
            print ("Opção inválida")
            continue