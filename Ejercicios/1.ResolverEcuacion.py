#Programa que resuelva una ecuacion de segundo grado

print('Resolver ecuacion')
a = int(input("Ingrese valor a:\t"))
b = int(input("Ingrese valor b:\t"))
c = int(input("Ingrese valor c:\t"))
sol1 = (-b+((b**2)-(4*a*c))**(1/2))/(2*a)
sol2 = (-b-((b**2)-(4*a*c))**(1/2))/(2*a)
print('solucion 1:\t', sol1)
print('solucion 2:\t', sol2)
