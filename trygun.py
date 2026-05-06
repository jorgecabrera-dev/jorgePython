try:
    edad = int(input("Ingrese su edad: "))
except ValueError as mostrarError:
    print("Solo debe ingresar números enteros")    
    print(mostrarError)