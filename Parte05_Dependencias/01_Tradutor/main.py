# Importando a biblioteca instalada

from translate import Translator

# Importa biblioteca os

import os

def limpar ():
    os.system ("cls" if os.name == "nt" else "clear")

def traduzir (texto):
    tradutor = Translator (to_lang = "pt")
    return tradutor.translate (texto)

def main ():
    limpar ()

    texto = input ("Informe o texto a ser traduzido: ")
    print (f"\n Texto traduzido: \n {traduzir(texto)}")

if __name__ == "__main__":
    main () 