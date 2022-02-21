# Listas list()
# Inicializacion []
# Listas no tiene un espacio definido

list1 = [1,2,3,4,5,6,7,8,9,10]

list2 = ['a', 'b', 'c', 85, 74, True, 2.45]

# Largo de lista
print(len(list2))
# Acceder a los elementos de la lista
print(list2[2])
print(list2[4])

# Cambiar valores de la lista
list2[5] = False
print(list2)

# Indexacion en intervalos
print(list2[1:3])
print(list2[::-1])

# LISTA DE ALUMNOS
alumnos = ['Jose', 'Andres', 'Juan', 'Marco', 'Pablo']

#obtener nueva lista con las dos ultimas personas
alumnos2 = alumnos[3:]
print(alumnos2)

#agregar a la lista
alumnos2.append('Fernando')
print(alumnos2)

#agregar en otra posicion
alumnos2.insert(1, 'Bryan')
print(alumnos2)

#Agregar lista a otra lista
alumnos2.extend(['Ana', 'Ernesto'])
print(alumnos2)

#quitar elementos
#pop recibe el indice a eliminar
#si no se pasa indice, elimina el ultimo
alumnos2.pop(2)
print(alumnos2)

#retirar valor especifico
alumnos2.remove('Bryan')
print(alumnos2)

#que pasa si hay elementos iguales?
alumnos2.extend(['Lori', 'Lori'])
print(alumnos2)
alumnos2.remove('Lori')
print(alumnos2) #solo elimina el ultimo

#operador
print('Ana' in alumnos2)
print('Raul' in alumnos2)

#hacer copia de lista
copiaAlumno = alumnos2[::]
print(copiaAlumno)
copiaAlumno2 = alumnos2.copy()

#invertir
print(copiaAlumno[::-1])
copiaAlumno2.reverse()
print(copiaAlumno2)

#encontrar indice
print(copiaAlumno.index('Ana'))

#que pasa si solicito un indice de un elemento inexistente
#print(copiaAlumno.index(80)) #error

#ordenar lista
#mismo tipo de dato
copiaAlumno.sort()
print(copiaAlumno)

list3 = [1, 5, 78, 25]
list3.sort(reverse=True) #False = ascendente
print(list3)

text = 'las universidades piensan las volver a la presencialidad'
listadeTexto = list(text)
print(listadeTexto)

#separar en palabras
palabra = text.split(' ')
print(palabra)

#numero de veces que una palabra esta en la lista
print(palabra.count('las'))

#join
saludo = 'hola'
oracion = saludo.join([' buenas', ' tardes'])
print(oracion)
#51