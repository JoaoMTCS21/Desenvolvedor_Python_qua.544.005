# Classe

class Pessoa:

    # Construtor

    def __init__(self, nome, idade, email, cpf):

        # Atributos

        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf

    def exibir_dados(self):
        print (f"Nome: {self.nome}")
        print (f"Idade: {self.idade}")
        print (f"E-mail: {self.email}")
        print (f"CPF: {self.cpf}")

def main ():

    # Instanciar a classe

    usuario = Pessoa (nome = "", idade=0, email = "", cpf = "" )

    # Insere valores nos atributos

    usuario.nome = input ("Informe um nome: ") .strip () . title ()
    usuario.idade = int ( input ("Informe a idade: "))
    usuario.email = input ( "Informe um email: ") .strip() .title()
    usuario.cpf = input ("Informe o cpf: ") .strip()

# Exibe os atributos na tela

    usuario.exibir_dados()

if __name__ == "__main__":
    main ()