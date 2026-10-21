# Dicionário

usuario = {
    'nome' : "Fulano de Tal",
    'idade' : 18,
    'email' : "fulano@gmail.com"
}

# Usuário informa o nome de uma nova chave

nova_chave = input ("Informe o nome de uma nova chave: ") .strip () .lower()

# Usuário informa uma nova chave

usuario[nova_chave] = input ("Informe o valor de uma nova chave: ") .strip ()

# Exibe o dicionário

for chave, valor in usuario.items ():
    print (f"{chave.capitalize()}: {valor}. ")