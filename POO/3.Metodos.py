# Metodos de clase y metodos estaticos
# Metodo de clase: requieren tener una instancia
# Metodo estatico: no requiere instancia de la clase
class Carro:
    def __init__(self, placa='ABC-123', color='rojo'):
        self.placa = placa,
        self.color = color

    def rodar(self):
        print(f'Soy el auto {self.placa} y de color {self.color}')

    @staticmethod #override
    def rodarEstatico(velocidad):
        print(f'Velocidad actual: {velocidad}')

    @classmethod
    def velocimetro(cls, velocidad):
        print(f'Velocidad actual: {velocidad}')

carro1 = Carro()
carro2 = Carro(placa='BDC-567', color='azul')

carro1.rodar()
carro1.rodarEstatico()

#sin necesidad de crear el objeto
Carro.rodarEstatico('20 km/h')