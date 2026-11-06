import os

from model import CarroVoador

def limpar ():
    os.system ("cls" if os.name == "nt" else "clear")

def main ():

    carro_voador = CarroVoador (
        cambio=True,
        estepe=False,
        porta_malas=False,
        volante=True,
        retrovisor=True,
        buzina=True,
        escapamento=True,
        asa=True,
        turbina=True,
        aerofolio=True,
        cauda=True,
        manche=True,
        caixa_preta=True
    )



if __name__ == "__main__":
    main ()