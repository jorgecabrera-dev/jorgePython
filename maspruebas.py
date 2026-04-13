nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))

print('Hola', nombre)

if edad >= 18:
    print ('Es mayor de edad')
else:
    print ('Es menor de edad')

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2

print('El resultado de la suma de ambos números es: ', suma)
print('El resultado de la resta de ambos números es: ', resta)
print('El resultado de la multiplicación de ambos números es: ', multi)
print('El resultado de la división de ambos números es: ', div)

afir = input('¿Hoy está lloviendo?: (si/no)')

if afir == 'si':
    print('No olvides llevar tu paraguas')
elif afir == 'no':
    print('¡Cuídate del sol!')
else:
    print('Respuesta inválida')

        