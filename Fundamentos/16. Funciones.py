# Funciones
# def

def saludar():
    print('Hola')

saludar()

edades = [18,5,20,22,17,14,2]

def esMayorEdad(edad: int):
    if edad >= 18:
        return True
    return False

for edad in edades:
    print(esMayorEdad(edad))

# Varios parametros
def saludo(nombre: str, apellido):
    return f'Saludos {nombre} {apellido}'

print(saludo("Jose", "Verdezoto"))

#parametros por defecto
def saludos(nombre= 'Juan', apellido= 'Moran'):
    return f'Hola {nombre} {apellido}'

print(saludos())
print(saludos('Marco'))
print(saludos(apellido='Caicedo'))
print(saludos("Fernando", "Real"))

# funcion dentro de funcion
def saludo2():
    print('Hola a todos')
    print(saludos())

saludo2()

# Documentacion

def calcularCubo(numero:int):
    '''
    Permite calcular el cubo de un numero
    numero: numero entero
    return: el cubo de la entrada
    '''

    return numero**3

print(calcularCubo(3))
print(calcularCubo.__doc__)

# funciones args
# *args

def listarAlumnos(*alumnos):
    print(f'Alumno: {alumnos}')

listarAlumnos('Jose')
listarAlumnos('Juan', 'Jose', 'Marco')

def listarAlumnos2(*alumnos):
    for alumno in alumnos:
        print(f'Alumno: {alumno}')

listarAlumnos2('Jose')
listarAlumnos2('Juan', 'Jose', 'Marco')

# **kargs
#numero indefinido de parametros
def listarAlumnos3(**alumnos):
    print('La edad es: ', alumnos['edad'])

listarAlumnos3(nombre='Jose', apellido='Verdezoto', edad=22)