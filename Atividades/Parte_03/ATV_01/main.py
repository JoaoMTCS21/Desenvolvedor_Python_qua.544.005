# TODO - ATIVIDADE - 01
'''
Crie um programa que calcule o peso de uma pessoa em um planeta do sistema solar escolhido por ela
'''

# NOTE: pesquisar pela aceleração da gravidade em cada planeta.
# NOTE: inclua a Lua na lista de planetas

import os

os.system ("cls" if os.name == "nt" else "clear")


def main():
    gravidade_terra = 9.81

    planetas = {
        "mercurio": 3.70,
        "venus": 8.87,
        "terra": 9.81,
        "lua": 1.62,
        "marte": 3.71,
        "jupiter": 24.79,
        "saturno": 10.44,
        "urano": 8.69,
        "netuno": 11.15,
        "plutao": 0.62,
    }

    obter_gravidade = lambda nome: planetas.get(nome.lower())

    print("Planetas disponíveis: Mercurio, Venus, Terra, Lua, Marte, Jupiter, Saturno, Urano, Netuno, Plutao")
    planeta = input("Escolha um planeta: ").strip()

    gravidade = obter_gravidade(planeta)

    if gravidade is None:
        print("Planeta inválido. Tente novamente.")
        return

    try:
        peso_terra = float(input("Digite seu peso na Terra em kg: ").replace(",", "."))
    except ValueError:
        print("Valor inválido. Digite apenas números.")
        return

    peso_planeta = peso_terra * (gravidade / gravidade_terra)

    print(f"Seu peso em {planeta.capitalize()} é: {peso_planeta:.2f} kg")


if __name__ == "__main__":
    main()


