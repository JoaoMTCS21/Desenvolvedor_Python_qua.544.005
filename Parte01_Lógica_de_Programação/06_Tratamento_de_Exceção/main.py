# Tratamento de Exceção

try: 
    nome = input ("Informe seu nome: ") .strip () .title ()
    idade = int (input ("Informe sua idade: "))

    print (f"Nome do Usuário: {nome}")
    print (f"Idade do Usuário: {idade} anos.")
except Exception as e:
    print ("Não foi possível executar a ação !")
finally:
    print ("Programa finalizado com sucesso !")