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
    print ("3 - Excluir usuário")
    print ("4 - Gravar dados cadastrados em um arquivo .json")
    opcao = input ("Opção desejada: ") .strip ()

    os.system ("cls" if os.name == "nt" else "clear")

    match opcao:

        case "1":

            usuario = {}

            usuario ['nome'] = input ("Informe o nome: ") .strip () .title ()
            usuario ['idade'] = int ( input ("Informe a idade: "))
            usuario ['email'] = input ("Informe o email: ") .strip() .lower()
            usuario ['cpf'] = input ("Informe o cpf: ") .strip()

            usuarios.append(usuario)
            os.system ("cls" if os.name == "nt" else "clear")
            
            
            print (f"{usuario.get ('nome')} cadastrado com sucesso!")  
            continue

        case "2":

            

