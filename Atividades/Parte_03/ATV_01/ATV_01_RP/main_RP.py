from modulo_RP import limpar, peso_astro

def main ():
    astros = {
        'mercurio': 3.73,
        'vênus': 8.73,
        'terra': 9.8,
        'lua': 1.62,
        'marte': 3.73,
        'jupiter': 24.92,
        'saturno': 10.5,
        'urano': 8.73,
        'netuno': 11.77
    }

    limpar ()

    massa = float ( input ("Informe sua massa: ") .replace (",","."))

    for chave, valor in astros.items():
        print (f"{chave.upper()}:")
        print (f"Gravidade: {valor} m/s²")
        print (f"Peso: {peso_astro(massa, valor):.2f}n")
        print (f"{'-' * 40}")

if __name__ == "__main__":
    main()