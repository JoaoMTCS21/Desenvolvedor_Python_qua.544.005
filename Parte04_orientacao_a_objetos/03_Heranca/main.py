import os

from model import PessoaFisica, PessoaJuridica

def limpar ():
    os.system ("cls" if os.name == "nt" else "clear")

def main ():

    # Instancia as classes

    usuario = PessoaFisica (nome = "", cpf = "", email = "", telefone = "", endereco = "")
    empresa = PessoaJuridica (cnpj = "", razao_social = "", nome_fantasia = "", email = "", telefone = "", endereco = "")

    # Informa os dados usuário

    limpar ()

    print (f"{'-' * 20} Informe os dados do usuário {'-' * 20}\n")
    usuario.nome = input ("Informe o nome do usuário: ") .strip () .title ()
    usuario.cpf = input ("Informe o nome do cpf: ") .strip ()
    usuario.email = input ("Informe o nome do e-mail: ") .strip () .lower ()
    usuario.telefone = input ("Informe o nome do telefone: ") .strip () 
    usuario.endereco = input ("Informe o nome do endereço: ") .strip () 

    # Informa os dados da empresa

    limpar ()
    print (f"{'-' * 20} Informe os dados da empresa {'-' * 20}")
    empresa.razao_social = input (" Informe a razão social: ") .strip ()
    empresa.nome_fantasia = input (" Informe o nome: ") .strip () .title()
    empresa.cnpj = input (" Informe a CNPJ: ") .strip ()
    empresa.email = input (" Informe a e-mail: ") .strip () .lower ()
    empresa.telefone = input (" Informe o telefone: ") .strip ()
    empresa.endereco = input (" Informe o endereço: ") .strip ()

    # Exibe dados das pessoas

    limpar ()
    usuario.exibir_dados()
    empresa.exibir_dados()


if __name__ == "__main__":
    main ()