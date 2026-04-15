cantidad = int(input('Ingrese la cantidad de notas a calcular: '))

suma = 0

for i in range(cantidad):
    nota = float(input('Ingrese la nota: '))
    suma += nota

promedio = suma / cantidad 

print('El promedio de las notas es:', promedio)

if promedio >= 4:
    print('El alumno aprobó')
else:    
    print('El alumno reprobó')