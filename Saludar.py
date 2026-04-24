def saludar(nombre):
    print ("Hola mundo,", nombre)
    return "Se termino la funcion"

nombre = input("Ingrese su nombre: ")
otro = saludar(nombre)

otro = otro.upper() # Convierte en mayusculas

print(otro)