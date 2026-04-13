nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))

print('Hola', nombre)

if edad >= 18:
    print ('Es mayor de edad')
else:
    print ('Es menor de edad')

afir = input('¿Hoy está lloviendo?: (si/no)')

if afir == 'si':
    print('No olvides llevar tu paraguas')
elif afir == 'no':
    print('¡Cuídate del sol!')
else:
    print('Respuesta inválida')

        