# print('hola Enrique')

# # creando variables

# titulo = 'clima de hoy' # String
# diaDelMes = 13 # Int
# mes = 4 # Int

# temperatura = 22.3 # Float

# llueve = False # Boolean

# print(titulo)
# print('Temperatura actual: ', temperatura, 'grados')
# print(diaDelMes, '-', mes)

# if llueve:
#     print('Tiene que llevar paraguas')
# else:
#     print('Puede llevar polera sin mangas')



# pedir password y pin
# pida al usuario password en palabras que debe ser "temu"
# además pida el pin que debe ser 3435
# los dos deben estar correctos para acceder al sistema

pas = input('Ingrese su password (solo letras): ')
pin = int(input('Ingrese su pin (solo números): '))

if pas == 'temu' and pin == 3435:
    print('acceso concedido')
else:
    print('password o pin incorrectos')