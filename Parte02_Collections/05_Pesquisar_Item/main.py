# Lista

cidades = [
    "Taguatinga",
    "Plano Piloto",
    "Santa Maria",
    "Gama",
    "Ceilandia",
    "Taguatinga",
    "Gama",
    "Ceilandia",
    "Plano Piloto",
    "Brazlândia",
    "Planaltina",
    "Santa Maria"
]

# Usuário informa o item a ser pesquisado

item = input ("Informe a cidade a ser pesquisada: ") .strip () .title ()

# Verifica quantas vezes o termo foi encontrado e o informa na tela

print (f"{item} foi encontrado {cidades.count(item)} vezes na lista.")