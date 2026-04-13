# calcular el puntaje de crédito
# debe calcular qué tanto crédito tiene una persona
# en cierta entidad financiera, deberá considerar
# cantidad de ingresos, nivel educacional y nacionalidad
# cantidad de ingresos
# 500.000 a 1.000.000 : 300.000
# 1.000.000 a 1.500.000 : 650.000
# 1.500.001 o más : 1.000.000
# Nivel educacional
# Básico : x1, medio : x1.3, superior : x1.5
# Nacionalidad
# Chilena : + 300.000, extranjero : + 0

sueldo = int(input('Ingrese su sueldo: '))
print('')
print ('1. Básico')
print ('2. Medio')
print ('3. Superior')
nivel = int(input('Ingrese su nivel educacional: '))

nac = input('Ingrese su nacionalidad (chilena/otra)')

credito = 0
if sueldo >= 500000 and sueldo <= 1000000:
    credito = credito + 300000
elif sueldo >= 1000000 and sueldo <= 1500000:
    credito = credito + 650000
elif sueldo >= 1500001:
    credito = credito + 1000000
else:
    print('')
    
if nivel == 1:
    print('')
elif nivel == 2:
    credito = credito * 1.3
elif nivel == 3:
    credito = credito * 1.5

if nac == 'chilena':
    credito = credito + 300000
else:
    print ('No tiene bono por nacionalidad')

print ('Su crédito es de: ', credito)