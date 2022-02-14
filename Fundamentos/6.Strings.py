#String, str

#Asignasiones de unica linea
from unicodedata import numeric


x = 'Hola'
y = ' con todos'

#String de varias lineas
texto = '''libroe 
cervantes
en un pueblo
ahi esta el molino
'''

#print(texto)

#Operaciones
cadena1 = 'Python'
cadena2 = ' es un lenguaje de programacion'
numero1 = 5
#Concatenar, unir 2 strings

print(cadena1, '-', cadena2, numero1)

print(cadena1 + cadena2 + str(numero1))

cadena3 = cadena1 + cadena2
print(cadena3)

#Formated strings
nombre = 'Jose'
edad = 21
#1. = f'{variable}'
print(f'Hola mi nombre es {nombre} y mi edad es {edad}')
#2. Llama al metodo clase string .format
print('Hola mi nombre es {} y mi edad es {}'.format(nombre, edad))

#3. llama al metodor formar pero indicando posicion
print('Hola mi nombre es {0} y mi edad {1}'.format(nombre, edad))
#Con repeticion
print('Me llamo {0}, mi nombre es {0}'.format(nombre))
#4. con reasignacion de variables
print('Hola mi nombre es {sinNombre} y mi edad es {sinEdad}'.format(sinNombre = 'Jose', sinEdad = edad))

#Indexacion
#Jose
#|0|1|2|3|

cadenatexto = 'Curso de programacion'
print(cadenatexto[0])
print(cadenatexto[1])
print(len(cadenatexto))
print(cadenatexto[-3])
print(cadenatexto[3]+cadenatexto[4]+cadenatexto[9]+cadenatexto[14])

#indexacion en rangos
#[valor incluido: valor excluido]
print(cadenatexto[0:2])
print(cadenatexto[2:10])
print(cadenatexto[2:20:2])
print(cadenatexto[2:])
print(cadenatexto[:3])
print(cadenatexto[::-1])
print(cadenatexto.upper()) #ver metodos w3school
print(cadenatexto.lower())
print(cadenatexto.find('de')) #devuelve el primer indice
print(cadenatexto.startswith('Curso'))
print(cadenatexto.startswith('Hola'))
print(cadenatexto.endswith('programacion'))
print(cadenatexto.endswith('hola'))
