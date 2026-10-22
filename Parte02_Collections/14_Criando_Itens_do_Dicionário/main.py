# Biblioteca 

import os

# List de usuários vazia

usuarios = []

# Limpar o terminal

os.system ("cls" if os.name == "nt" else "clear")

# Loop

while True:

    # Menu

    print ("1 - Cadastrar novo usuário")
    print ("2 - Exibir lista de usuários")
    print ("3 - Sair do programa")
    opcao = input ("Opção desejada: ") .strip()

    # Verifica a opção escolhida

    match opcao:

        case "1":

            # Cria novo dicionário

            usuario = {}

            # Insere os dados no dicionário

            usuario ['nome'] = input ("Informe o nome: ") .strip () .title ()
            usuario ['idade'] = int ( input ("Informe a idade: "))
            usuario ['email'] = input ("Informe um email: ") .strip() .lower()
            usuario ['cpf'] = input ("Informe o CPF: ") .strip ()

            # Adiciona o usuário a lista

            usuarios.append(usuario)

            # Mensagem de sucesso

            print (f"{usuario.get('nome')} cadastrado com sucesso!")
            continue

        case "2":

            # Exibe a lista de usuários:

            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print (f"{chave.capitalize()}: {valor}")
                print (f"{'-' * 40}")
            continue

        case "3":
            break

        case _:
            print ("Opção inválida.")
            continue

