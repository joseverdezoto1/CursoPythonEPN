# Tupla - tuple
# Inmutable 

tupla1 = (3,4,5,6,6)
print(tupla1)
print(type(tupla1))

#Acceder
print(tupla1[0])

#tupla1[0] = 8 es inmutable, no va a cambiar

#Tupla con diferentes tipos de datos
tupla2 = (True, 25, 'Hola')
print(tupla2)

#Averiguar si un elemento se encuentra o no en una lista
print(False in tupla2)
print('Chao' in tupla2)
print(25 in tupla2)
print(100 not in tupla2)

#Metodos de la tupla
print(tupla1.index(3))
print('Tamano de una tupla ', len(tupla1))
print('contar cuantos 6 hay en la tupla ', tupla1.count(6))

#Descompresion
dimensiones = (500,600)
largo, ancho = dimensiones
print(largo)
print(ancho)

#Convertir de lista a tupla
lista = [1,2,3]
miTupla = tuple(lista)
print(miTupla)