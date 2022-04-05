# Herencia

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def registrado(self):
        print('Personaje registrado!')

class Superheroe(Personaje):
    def __init__(self, nombre, virtud='Bondadoso'):
        super().__init__(nombre)
        self.virtud = virtud

    def salvarMundo(self):
        print('Estoy salvando al mundo')

personaje = Personaje('Random')
personaje.registrado()
super = Superheroe('Spiderman', 'Honesto')
super.registrado()
super.salvarMundo()

#33