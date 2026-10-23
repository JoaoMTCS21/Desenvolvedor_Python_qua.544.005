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
    print ("2 - Gravar arquivo JSON")
    print ("3 - Abrir arquivo JSON")
    print ("4 - Sair do programa")
    opcao = input ("Opção desejada: ") .strip ()
    os.system ("cls" if os.name == "nt" else "clear")

    match opcao:

        case "1":

            # Novo dicionário

            usuario = {}

            # Insere os dados do usuário

            usuario ['nome'] = input ("Informe o nome: ") .strip () .title ()
            usuario ['idade'] = int ( input ("Informe a idade: "))
            usuario ['email'] = input ("Informe o email: ") .strip() .lower()
            usuario ['cpf'] = input ("Informe o cpf: ") .strip()
            usuario ['telefone'] = input ("Informe o telefone: ") .strip()

            # Adiciona o usuário a lista

            usuarios.append(usuario)
            os.system ("cls" if os.name == "nt" else "clear")

            # mensagem de confirmação

            print (f"{usuario.get ('nome')} cadastrado com sucesso!")
            continue

        case "2":

            # Exibe os usuários cadastrados

            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print (f"{chave.capitalize()}: {valor}")
                print (f"{'-' * 40}")

            # Pergunta ao usuários se deseja prosseguir

            prosseguir = input ("Deseja gravar os dados ? (s/n)") .strip() .lower()

            if prosseguir == "s":
                os.system ("cls" if os.name == "nt" else "clear")
                arquivo = input ("Informe o nome do arquivo: ") .strip ()
                with open (f"16_JSON/{arquivo}.json", "w", encoding = "utf-8") as f:
                    json.dump(usuarios, f)
                print ("Arquivo json gravado com sucesso !")
                continue

            else: 
                os.system ("cls" if os.name == "nt" else "clear")
                continue

        case "3":
             os.system ("cls" if os.name == "nt" else "clear")
             try:
                 # Informa o nome o arquivo que deseja abrir

                 abrir = input ("Informe o nome do arquivo que deseja abrir: ") .strip()

                 # Abre o arquivo
                 
                 with open (f"16_JSON/{abrir}.json" , "r" , encoding = "utf-8") as f:
                     usuarios = json.load(f)

                 #Exibir os dados do arquivo

                 for usuario in usuarios:
                     for chave, valor in usuario.items():
                         print (f"{chave.capitalize()}: {valor}")
                     print (f"{'-' * 40}")
                 continue

             except Exception as e:
                 print (f"Não possível abrir o arquivo. {e}.")
             continue
        
        case "4":
            break

        case _:
            print ("Opção inválida")