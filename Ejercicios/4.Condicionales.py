#palindromo

texto = input('Ingrese el texto:\t')

print('De izquierda a derecha: '+texto)
print('De derecha a izquierta: '+texto[::-1])

if texto == texto[::-1]:
    print('Ingresaste un palindromo')
elif texto.lower() == texto[::-1].lower():
    print('Palindromo ignorando mayusculas')
elif texto.replace(' ','') == texto[::-1].replace(' ',''):
    print('Palindromo ignorando espacios')
else:
    print('no es palindromo')