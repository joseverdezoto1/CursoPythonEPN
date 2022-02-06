#Enteros
#int

import math as math #para raiz2

num1 = input('Ingresa un numero\t')
print(type(num1)) #tipo string
num1 = int(num1) #conversion a entero
print(num1+20) #tipo int

#en una sola linea
num2 = int(input('Ingrese un valor\t'))
print(num1+20)

#
num3 = int(True)
print(num3)

#Operadores numericos
a,b=2,3
print('suma: ',a+b)
print('resta: ',a-b)
print('multiplicacion: ',a*b)
print('division: ',a/b)
print('potencia: ',2**3) #2 al cubo
print('modulo: ',10%2)
print('division entera', 10//3)
print('raiz: ',64**(1/2))
print('raiz2: ', math.sqrt(64)) #se puede importar una libreria

#flotantes
#mismos operadores
numeroFlotante = float(input('Ingresa un decimal:\t'))
print(numeroFlotante)