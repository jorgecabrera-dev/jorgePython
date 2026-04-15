# ejemplo y explicación de for:

# for i in range(5):
#    print(i + 1)

# pedir un número al usuario:
# mostrar un saludo esa cantidad de veces:

# num = int(input('Ingrese un número: '))

# for i in range(num):
#    print(i + 1, 'Hola Mariano')

# pedr un número al usuario:
# mostrar la tabla de multiplicar
# de ese número hasta 10

# num = int(input('Ingrese un número: '))

# for i in range(10):
#    print(num, 'x', i + 1, '=', num * (i + 1))


# num = int(input('Ingrese un número: '))

# for i in range(1, 11):
#    print(num, 'x', i, '=', num * i)


# pedir un número al usuario:
# mostrar la suma desde el 1
# hasta ese número
# ej: 3 --> 1 + 2 + 3 = 6

# num = int(input('Ingrese un número: '))
# suma = 0
# for i in range(num):
#    suma += i + 1

# print('El resultado de la suma es:', suma)


# pedir la cantidad de notas al usuario
# luego pedir cada nota individualmente
# calcular el promedio de todas las notas
# mostrar si aprueba o no


# cantidad = int(input('Ingrese la cantidad de notas a calcular: '))

# suma = 0

# for i in range(cantidad):
#    nota = float(input('Ingrese la nota: '))
#    suma += nota

# promedio = suma / cantidad 

# print('El promedio de las notas es:', promedio)

# if promedio >= 4:
#    print('El alumno aprobó')
# else:    
#    print('El alumno reprobó')


# nombre = input('Ingrese su nombre: ')

# cantidad = 0

# for i in nombre:
#    print(i)
#    cantidad += 1

# print('La cantidad de letras es:', cantidad)



nombre = input('Ingrese su nombre: ')

vocal = 0
consonante = 0

for i in nombre:
    print(i)
    if i in "AEIOUaeiou":
        vocal += 1
    else:
        consonante += 1

print('La cantidad de vocales es:', vocal)
print('La cantidad de consonantes es:', consonante)


