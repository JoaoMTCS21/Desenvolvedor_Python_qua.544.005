# TODO - ATIVIDADE - 02
'''
Crie um programa em que o usuário informe um número inteiro e o programa retorne a sequência Fibonacci
'''
import os

os.system ("cls" if os.name == "nt" else "clear")

def main():
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Valor inválido! Digite apenas números inteiros.")
        return

    if numero < 0:
        print("Digite um número maior ou igual a zero.")
        return

    prox_fibonacci = lambda anterior, atual: (atual, anterior + atual)

    fibonacci = []
    a, b = 0, 1

    while a <= numero:
        fibonacci.append(a)
        a, b = prox_fibonacci(a, b)

    if fibonacci:
        print(f"Sequência Fibonacci até {numero}: {fibonacci}")
    else:
        print(f"Não há sequência Fibonacci até {numero}.")


if __name__ == "__main__":
    main()


