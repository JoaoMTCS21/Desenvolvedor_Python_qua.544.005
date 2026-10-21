# Biblioteca

import os

# Limpar terminal

os.system ("cls" if os.name == "nt" else "clear")

# Lista

usuario = {
    'nome' : "Alex Machado",
    'idade' : 41,
    'altura' : 1.72,
    'email': "alex@gmail.com",
    'cpf' : "123.456.789-12",
    'telefone' : "(61) 98761-4321"
}

# Exibe o valor específico

print (f"Nome: {usuario['nome']}")

# Outra forma, uma que não faz o programa parar, mesmo que variavel não exista

print (f"E-mail: {usuario.get ('email')}") 

# Outra forma, uma que percorre o dicionário

for chave, valor in usuario.items():
    print (f"{chave.capitalize()}: {valor}. ")