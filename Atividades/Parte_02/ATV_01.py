# TODO - Atividade - 02
"""
Crie um programa que faça as seguintes operações:
- Cadastra novo usuário (nome, email, telefone, cpf)
- Lista todos os usuários cadastrados
- Altera os dados de um usuário
- Exclui um usuário
- Grava os dados de todos os usuários em um .json
- Abre arquivo .json e lista todos os usuários cadastrados nele
"""

import os
import json

os.system ("cls" if os.name == "nt" else "clear")

usuarios = []

while True:

    print ("1 - Cadastrar um novo usuário")
    print ("2 - Exibir usuários cadastrados")
    print ("3 - Alterar os dados de um usuário")
    print ("4 - Excluir usuário")
    print ("5 - Gravar dados cadastrados em um arquivo .json")
    print ("6 - Escolher e exibir o conteúdo do arquivo .json")
    print ("7 - Encerrar o programa")
    opcao = input ("Opção desejada: ") .strip ()

    os.system ("cls" if os.name == "nt" else "clear")

    match opcao:

        case "1":

            usuario = {}

            usuario ['nome'] = input ("Informe o nome: ") .strip () .title ()
            usuario ['idade'] = int ( input ("Informe a idade: "))
            usuario ['telefone'] = input ("Informe o número de telefone: ") .strip()
            usuario ['email'] = input ("Informe o email: ") .strip() .lower()
            usuario ['cpf'] = input ("Informe o cpf: ") .strip()

            usuarios.append(usuario)
            os.system ("cls" if os.name == "nt" else "clear")
            
            print (f"{usuario.get ('nome')} cadastrado com sucesso!")  
            continue

        case "2":

            if not usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for usuario in usuarios:
                    for chave, valor in usuario.items():
                        print (f"{chave.capitalize ()}: {valor}")
                    print (f"{'-' * 40}")
            continue

        case "3":
            if not usuarios:
                print("Nenhum usuário cadastrado para alterar.")
                continue

            nome_busca = input("Informe o nome do usuário que deseja alterar: ").strip().title()
            usuario_encontrado = None

            for u in usuarios:
                if u.get('nome') == nome_busca:
                    usuario_encontrado = u
                    break

            if not usuario_encontrado:
                print(f"Usuário '{nome_busca}' não encontrado. Encerrando alteração.")
                continue

            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"--- Editando usuário: {usuario_encontrado.get('nome')} ---")
                for chave, valor in usuario_encontrado.items():
                    print(f"{chave.capitalize()}: {valor}")
                print("-" * 40)

                chave_escolhida = input("Informe qual dado deva ser alterado (ou pressione Enter para encerrar): ").strip().lower()

                if not chave_escolhida:
                    print("Encerrando alterações para este usuário.")
                    break

                if chave_escolhida in usuario_encontrado:
                    novo_valor = input(f"Informe o que vai ser inserido no lugar de '{chave_escolhida}': ").strip()
                    
                    if chave_escolhida == 'idade':
                        novo_valor = int(novo_valor)
                    elif chave_escolhida == 'nome':
                        novo_valor = novo_valor.title()
                    elif chave_escolhida == 'email':
                        novo_valor = novo_valor.lower()

                    usuario_encontrado[chave_escolhida] = novo_valor
                    print("Dado alterado com sucesso!")
                else:
                    print("Chave inválida!")

                prosseguir_alterando = input("Deseja alterar algo a mais neste usuário? (s/n): ").strip().lower()
                if prosseguir_alterando != "s":
                    break
            continue

        case "4":
            if not usuarios:
                print("Nenhum usuário cadastrado.")
                continue

            nome_busca = input("Informe o nome do usuário para exclusão de chave: ").strip().title()
            usuario_encontrado = None

            for u in usuarios:
                if u.get('nome') == nome_busca:
                    usuario_encontrado = u
                    break

            if not usuario_encontrado:
                print("Usuário não encontrado.")
                continue

            for chave, valor in usuario_encontrado.items():
                print(f"{chave}: {valor}")

            chave_escolhida = input("Informe a chave a excluir: ").strip().lower()

            if chave_escolhida in usuario_encontrado:
                del usuario_encontrado[chave_escolhida]
                print("Chave excluída com sucesso!")
            else:
                print("Chave não encontrada.")
            continue

        case "5":
            if not usuarios:
                print("Nenhum usuário para gravar.")
                continue

            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print (f"{chave.capitalize()}: {valor}")
                print (f"{'-' * 40}")

            prosseguir = input ("Deseja gravar os dados ? (s/n): ") .strip() .lower()
         
            if prosseguir == "s":
                os.system ("cls" if os.name == "nt" else "clear")
                arquivo = input ("Informe o nome do arquivo: ") .strip ()
                
                os.makedirs("ATV_01", exist_ok=True)
                
                with open (f"ATV_01/{arquivo}.json", "w", encoding = "utf-8") as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=4)
                    
                print ("Arquivo json gravado com sucesso !")
            continue

        case "6":
            os.system ("cls" if os.name == "nt" else "clear")
            abrir = input ("Informe o nome do arquivo que deseja abrir: ") .strip()
                        
            try:
                with open (f"ATV_01/{abrir}.json" , "r" , encoding = "utf-8") as f:
                    usuarios = json.load(f)
                
                for usuario in usuarios:
                    for chave, valor in usuario.items():
                        print (f"{chave.capitalize()}: {valor}")
                    print (f"{'-' * 40}")
            except FileNotFoundError:
                print("Arquivo não encontrado.")
            continue

        case "7":
            print("Programa encerrado !")
            break
            
        case _:
            print("Opção inválida! Escolha um número de 1 a 7.")
            continue