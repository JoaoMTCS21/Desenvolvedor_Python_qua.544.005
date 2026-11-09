class Motor:
    def __init__ (self, potencia):
        self.__potencia = potencia

    @property
    def potencia (self):
        return self.__potencia

    @potencia.setter
    def potencia (self, potencia):
        self.__potencia = potencia

    def info (self):
        return f"Potência: motor de {self.__potencia} cv."

class Carro:
    def __init__ (self, fabricante, modelo, ano, cor, potencia):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__motor = Motor(potencia)

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self.__fabricante = fabricante

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, motor):
        self.__motor = motor

    def exibir_detalhes (self):
        return f"Fabricante: {self.__fabricante} \n Modelo: {self.__modelo} \n Ano: {self.__ano} \n Cor: {self.__cor} \n Motor: {self.__motor.info()}"

