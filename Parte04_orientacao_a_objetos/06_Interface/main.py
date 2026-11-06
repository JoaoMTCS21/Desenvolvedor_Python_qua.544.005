# bibliotecas

import os
import random

from model import Conta


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():

    # instancia a classe Conta
    cc = Conta(
        titular="",
        cpf="",
        agencia="1010-1",
        n_conta=f"{random.randint(10000,99999)}-1",
        saldo=0.0
    )

    while True:
        limpar()
        print("=== BANCO ===")
        print("1 - Cadastrar titular")
        print("2 - Consultar conta")
        print("3 - Depositar")
        print("4 - Sacar")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cc.titular = input("Digite o nome do titular: ").strip().title()
                cc.cpf = input("Digite o CPF do titular: ").strip()
                print("Titular e CPF cadastrados com sucesso!")
                input("Pressione Enter para continuar...")

            case "2":
                cc.consultar_conta()
                input("Pressione Enter para continuar...")

            case "3":
                valor = float(input("Digite o valor do depósito: "))
                if valor > 0:
                    print(f"Saldo atual: R$ {cc.depositar(valor):.2f}")
                else:
                    print("Valor inválido para depósito.")
                input("Pressione Enter para continuar...")

            case "4":
                valor = float(input("Digite o valor do saque: "))
                if valor <= 0:
                    print("Valor inválido para saque.")
                elif valor > cc.saldo:
                    print("Saldo insuficiente para realizar o saque.")
                else:
                    print(f"Saldo atual: R$ {cc.sacar(valor):.2f}")
                input("Pressione Enter para continuar...")

            case "0":
                print("Encerrando o programa...")
                break

            case _:
                print("Opção inválida. Tente novamente.")
                input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()