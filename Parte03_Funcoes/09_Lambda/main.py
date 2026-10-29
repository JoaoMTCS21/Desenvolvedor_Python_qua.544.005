import os

# Lambdas

limpar = lambda: os.system ("cls" if os.name == "nt" else "clear")
area_triangulo = lambda b,h: (b*h)/2

# Função principal

def main ():
    limpar ()
    b = float ( input ("Informe a base: ") .replace (",","."))
    h = float ( input ("Informe a altura: ") .replace (",","."))
    limpar ()
    print (f"Área do triângulo: {area_triangulo (b,h)}.")

if __name__ == "__main__":
    main ()