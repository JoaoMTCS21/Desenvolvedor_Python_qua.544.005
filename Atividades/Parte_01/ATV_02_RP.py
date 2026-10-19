# TODO - Atividade - 02 - Respondida pelo professor
'''
Crie um programa em que o usuário informe uma única vez o nome e a idade, e em seguida, o programa exibe uma lista de filmes do cinema e suas respectivas salas e classificações indicativas.
O usuários deverá escolher a sala do filme desejado. Se estiver a idade mínima, o programa imprime o ingresso e encerra. Senão, o programa impede a entrada do usuário e retorna a lista para que o mesmo possa escolher outro filme.
'''

# Importe a biblioteca

import os

# Limpa o terminal

os.system("cls" if os.name == "nt" else "clear")

# Dados do usuário

nome = input("Digite seu nome: ") .strip () .title ()
idade = int(input("Digite sua idade: "))
idade_minima = None
# Loop

while True:
    # Menu de filmes
    print (f"{'-'*20} CINE COBRA {'-'*20}")
    print ("Sala 1 - A Roda Quadrada - Livre")
    print ("Sala 2 - A Volta Dos Que Não Foram - 12 Anos")
    print ("Sala 3 - As Tranças do Rei Careca - 14 Anos")
    print ("Sala 4 - Poeira em Alto Mar - 16 Anos")
    print ("Sala 5 - A Vingamça do Peixe Frito - 18 Anos")

# Usuário informa a sala do filme desejado

    sala = input ("Sala desejada: ") .strip()

# Atribui a idade mínima ao filme

    match sala:
         case "1":
            idade_minima = 0
         case "2":
            idade_minima = 12
         case "3": 
            idade_minima = 14
         case "4":
           idade_minima = 16
         case "5":
           idade_minima = 18
         case _:
           print ("Sala inexistente. ")
           idade_minima = idade + 1

    #Verifica a idade

    if idade >= idade_minima:
       print (f"Ingresso Imprimido para {nome}")
       print ("Tenha um bom filme !")
       break

    else:
       os.system("cls" if os.name == "nt" else "clear")
       print (f"Ingresso Negado para {nome}")
       print ("Você não possui idade mínima para er o filme !")
       print ("Por favor, escolha outro filme: ")
       continue