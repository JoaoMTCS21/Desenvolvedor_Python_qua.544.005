# TODO
'''
Crie um programa em que o usuário informe uma única vez o nome e a idade, e em seguida, o programa exibe uma lista de filmes do cinema e suas respectivas salas e classificações indicativas.
O usuários deverá escolher a sala do filme desejado. Se estiver a idade mínima, o programa imprime o ingresso e encerra. Senão, o programa impede a entrada do usuário e retorna a lista para que o mesmo possa escolher outro filme.
'''

import os

os.system("cls" if os.name == "nt" else "clear")

nome = input("Digite seu nome: ") .strip () .title ()
idade = int(input("Digite sua idade: "))

while True:
    print (f"Olá {nome}! Escolha a sala do filme:")
    print ("Sala 1 - Divertida Mente (Livre)")
    print ("Sala 2 - Homem-Aranha (Classificação: 12 anos)")
    print ("Sala 3 - Batman (Classificação: 14 anos)")
    print ("Sala 4 - Invocação do Mal (Classificação: 16 anos)")
    print ("Sala 5 - Coringa (Classificação: 18 anos)")
    
    escolha = input("Digite o número da sala desejada (1 a 5): ")

    if escolha == "1":
        print("INGRESSO GERADO!")
        print(f" Cliente: {nome}")
        print(" Filme: Divertida Mente (Sala 1)")
        break

    elif escolha == "2":
        if idade >= 12:
            print("INGRESSO GERADO!")
            print(f" Cliente: {nome}")
            print(" Filme: Homem-Aranha (Sala 2)")
            break
        else:
            print(f"Entrada proibida! Você tem {idade} anos e o filme exige 12 anos.")

    elif escolha == "3":
        if idade >= 14:
            print("INGRESSO GERADO!")
            print(f" Cliente: {nome}")
            print(" Filme: Batman (Sala 3)")
            break
        else:
            print(f"Entrada proibida! Você tem {idade} anos e o filme exige 14 anos.")

    elif escolha == "4":
        if idade >= 16:
            print("INGRESSO GERADO!")
            print(f" Cliente: {nome}")
            print(" Filme: Invocação do Mal (Sala 4)")
            break
        else:
            print(f"Entrada proibida! Você tem {idade} anos e o filme exige 16 anos.")

    elif escolha == "5":
        if idade >= 18:
            print("INGRESSO GERADO!")
            print(f" Cliente: {nome}")
            print(" Filme: Coringa (Sala 5)")
            break
        else:
            print(f"Entrada proibida! Você tem {idade} anos e o filme exige 18 anos.")

    else:
        print("Sala inválida! Tente novamente.")
