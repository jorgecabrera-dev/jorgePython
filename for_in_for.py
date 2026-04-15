# pida la cantidad de alumnos
# por cada alumno pida la cantidad de notas
# saque el promedio y muestre si aprueba o no
# muestre la cantidad de alumnos aprobados y reprobados

canA = int(input('Ingrese la cantidad de alumnos: '))
suma = 0
apro = 0
repro = 0

for i in range(canA):
    canN = int(input('Ingrese la cantidad de notas: '))
    nota = float(input('Ingrese la nota: '))
    suma += nota
    promedio = suma / canN
    if promedio >= 4:
        apro + 1
    else:
        repro + 1



    




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