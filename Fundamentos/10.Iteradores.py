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
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print('Valor de la posicion i:{} - j:{} es:{}'.format(i,j,matriz[i][j]))
        if matriz[i][j] == 2:
            matriz[i][j] = 10

print(matriz)