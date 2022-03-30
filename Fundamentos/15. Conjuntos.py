#set

conjunto1 = {1,2,3,4}
print(conjunto1)
print(type(conjunto1))

conjunto2 = {1,2,3,4,4}
print(conjunto2)

#Crear lista con elementos unicos
listaEjemplo = [14,15,16,63,63,63,89,75,14,15]
conjunto3 = set(listaEjemplo)
print(conjunto3)


# Es posible crear conjuntos no numericos?
conjunto4 = {'andres', 'bryan', 'cristo', 'andres'}
print(conjunto4)

#Conjuntos de diferentes tipos de datos
conjunto5 = {78, 54.5, True, False, 'Juan'}
print(conjunto5)

#Metodos
A = {1,2,3,4,5,6,7}
B = {3,4,5}

#Agregar elemento al conjunto
A.add(8)
print(A)

#tamano de un conjunto
print(len(A))

#eliminar elemento
A.discard(8)
print(A)

#update conjunto
#une lo de antes con los ingresados
A.update({6,7,8,9})
print(A)

#copiar un conjunto
C = A.copy()
print(C)

# pop
C.pop()
print(C)

#limpiar
C.clear()
print(C)

# Metodos entre dos conjuntos
print('Conjunto A: ',A)
print('Conjunto B: ',B)

#diferencia (A-B)
print(A.difference(B))

#union
D = {10}
print(A.union(D))

#interseccion
print(A.intersection(B))

#Diferencia simetrica
print(A.symmetric_difference(B))

# si dos conjuntos son disjuntos
print(A.isdisjoint(B))
E = {100, 200}
print(A.isdisjoint(E))

#si es subconjunto
print(B.issubset(A))

#si es superconjunto
print(A.issuperset(B))