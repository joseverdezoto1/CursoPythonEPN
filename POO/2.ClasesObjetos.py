# Clases con metodos y atributos

class Personaje:
    # Atributos
    # Constructor
    def __init__(self, nombre, tipo, edad): #self: le pertenece a la clase
        # Siempre se va a ejecutar
        # Es lo primero en ejecutarse
        self.nombrePersonaje = nombre
        self.tipo = tipo
        self.edad = edad
        
    # Metodos
    def saludar(self):
        print(f'Hola, soy un personaje\nMi nombre es: {self.nombrePersonaje}')

    # Getters y Setters
    def getNombrePersonaje(self):
        return self.nombrePersonaje
    def setNombrePersonaje(self, nuevoNombre: str):
        self.nombrePersonaje = nuevoNombre

personaje1 = Personaje('Batman', 'Heroe', 20)
personaje2 = Personaje('Spiderman', 'Heroe', 30)

print(personaje1.nombrePersonaje)
print(personaje2.nombrePersonaje)

personaje1.saludar()
personaje2.saludar()

print('Nombre antes del set ', personaje2.getNombrePersonaje())
personaje2.setNombrePersonaje('Venom')
print('Nombre despues del set ', personaje2.getNombrePersonaje)

#Instalar pip3 PENDIENTE