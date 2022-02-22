#Iteradores
#for, permite recorrer un iterable

frutas = ['pera', 'manzana', 'banana']

for frut in frutas:
    print(frut)

#Utilizar rangos numericos
for item in range(0,5):
    print('Elemento {}'.format(item))

matriz = [
    [0,1,0],
    [1,1,1],
    [0,0,2]
]

#anidados
for fila in matriz:
    for columna in fila:
        print(columna)

#anidados basados en indices
for fila in range(len(matriz)):
    for columna in range(len(fila)):
        print(matriz[fila][columna])
        #1:20