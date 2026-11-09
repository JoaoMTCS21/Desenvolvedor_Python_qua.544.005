import os

from model import Empresa, Departamento

def limpar ():
    os.system ("cls" if os.name == "nt" else "clear")

def main():
    limpar()

    departamento = Departamento("")
    empresa = Empresa(
        razao_social="",
        nome_fantasia="",
        cnpj="",
        departamento=departamento,
    )

    print("Dados da empresa que vai receber o departamento: ")
    empresa.razao_social = input("Informe a razão social: ").strip()
    empresa.nome_fantasia = input("Informe o nome fantasia: ").strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.departamento.nome = input("Informe o nome do departamento: ").strip()

    limpar()
    print(empresa.detalhes())


if __name__ == "__main__":
    main()