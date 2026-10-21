# Biblioteca

import os

# Dicionário

usuario = {
    'nome' : "Thomas Anderson",
    'idade' : 40,
    'email' : "mrandesson@gmail.com",
    'telefone' : "(61) 96666-6666"
}

# Limpar terminal

os.system ("cls" if os.name == "nt" else "clear")

# Loop

while True:

    # Exibe o dicionário

    for chave, valor in usuario.items():
        print (f"{chave}: {valor}")

    # Informa uma nova chave

    chave_escolhida = input ("Informe o nome da chave que deseja alterar ou Enter para encerrar: ") .strip() .lower()

    # Verifica se a chave é válida

    if chave_escolhida:

        #Informa um novo valor

        usuario [chave_escolhida] = input ("Informe o novo valor: ") .strip ()
        continue
    else:
        break
