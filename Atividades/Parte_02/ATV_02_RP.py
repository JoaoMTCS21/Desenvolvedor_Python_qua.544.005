# Bibliotecas

import os
import json

# Lista

usuarios = []

# Limpa terminal

os.system ("cls" if os.name == "nt" else "clear")

# Loop

while True:

    # Menu

    print ("1 - Cadastrar novo usuário")
    print ("2 - Listar usuários cadastrados")
    print ("3 - Alterar dados do usuário")
    print ("4 - Excluir um usuário")
    print ("5 - Gravar todos os usuários em um .json")
    print ("6 - Abrir arquivo .json")
    print ("7 - Sair do programa")
    opcao = input ("Opção desejada: ") .strip()

    os.system ("cls" if os.name == "nt" else "clear")

    match opcao:

        case "1":

            # Inicializar um novo dicionário

            usuario = {}

            # Informa os dados

            usuario ['nome'] = input ("Informe o nome: ") .strip () .title ()
            usuario ['idade'] = int ( input ("Informe a idade: "))
            usuario ['email'] = input ("Informe o email: ") .strip() .lower()
            usuario ['telefone'] = input ("Informe o número de telefone: ") .strip()
            usuario ['cpf'] = input ("Informe o cpf: ") .strip()

            # Adiciona um novo usuário na lista

            usuarios.append(usuario)
            os.system ("cls" if os.name == "nt" else "clear")

            # Exibir a mensagem de cadastro

            print (f"{usuario.get ('nome')} cadastrado com sucesso!")  

            continue

        case "2":

            for i, usuario in enumerate (usuarios):
                print (f"ID: {i}")
                for chave, valor in usuario.items():
                    print (f"{chave.capitalize()}: {valor}")
                print (f"{'-' * 40}")
            continue

        case "3":

            try:

                indice = int (input ("Informe o índice do usuário a ser alterado: "))
                for chave, valor in usuarios [indice] .items():
                    print (f"{chave.capitalize()}: {valor}.")
                chave = input ("Qual chave deseja alterar o valor? ") .strip () .lower()
                usuarios [indice] [chave] = input ("Informe o novo valor:") .strip()
                os.system ("cls" if os.name == "nt" else "clear")
                print (f"Dados de {usuarios[indice][chave]} de {usuarios [indice] .get('nome')} alterado com sucesso!")
                continue

            except Exception as e:

                print (f"Não foi possível atualizar os dados. {e}.")

        case "4":

            try:

                indice = int ( input ("Informe o ID a ser excluído: "))
                del usuarios [indice]
                os.system ("cls" if os.name == "nt" else "clear")
                print ("Usuário excluído com sucesso!")
                continue

            except Exception as e:

                print (f"Não foi possível excluir. {e}.")

        case "5":

            arquivo = input ("Informe o nome do arquivo: ") .strip ()
            with open (f"ATV_02_RP/{arquivo}.json","w",encoding = "utf-8" ) as f:
                json.dump(usuarios, f)
            os.system ("cls" if os.name == "nt" else "clear")
            print ("Dados gravados com sucesso!")
            continue


        case "6":

            try:

                arquivo = input ("Informe o arquivo que deseja abrir: ") .strip ()
                with open (f"ATV_02_RP/{arquivo}.json","r",encoding = "utf-8") as f:
                 usuarios = json.load (f)
                os.system ("cls" if os.name == "nt" else "clear")
                print ("Dados importados com sucesso!")
                continue

            except Exception as e:
                print (f"Não foi possível abrir o arquivo. {e}")

        case "7":
            print("Programa encerrado !")
            break

        case _:
            print ("Opção inválida.")
            continue