#Validar si los enlaces son correctos
#debe empezar con httpps:// y terminar con .com
link1 = 'https://www.epn.edu.ec.ecuador'
link2 = 'https://modemat.com'
link3 = 'https:/fis.edu.lat'

print('Empieza con https:// = ' + str(link1.startswith('https://')))
print('Termina con .com = '+ str(link1.endswith('.com')))
print('Empieza con https:// = '+ str(link2.startswith('https://')))
print('Termina con .com = '+ str(link2.endswith('.com')))
print('Empieza con https:// = '+ str(link3.startswith('https://')))
print('Termina con .com = '+ str(link3.endswith('.com')))