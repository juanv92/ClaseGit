# Asistente medico

print("TRIAJE")

try:
    # string ingresar nomre
    nombre = input("Ingrese su nombre: ")

    # int ingresar edad
    edad = int(input("Ingrese su edad: "))

    # float
    temperatura = float(input("Ingrese su temperatura: "))

    # string sintomas graves si/no
    sintomas = input("Tiene sintomas graves (si/no): ").lower()

    print("\nResultado del analisis:\n")

    if sintomas == "si":

        # ssintoma ecribir un sintoma
        detalle = input("Escriba el sintoma: ").lower()

        # OR detalle del sintoma
        if detalle == "dolor fuerte" or detalle == "dificultad al respirar" or detalle == "sangrado":
            print(nombre, "debe ir a URGENCIAS")
        else:
            print(nombre, "debe ir a consulta PRIORITARIA")

    elif sintomas == "no":
        print(nombre, "puede quedarse en CASA")

    else:
        print("Respuesta no valida")

    # OR si la temperatura es mayor a 39
    if temperatura >= 39 or sintomas == "si":

        # anidado si la edad es mayor o igual a 60
        if edad >= 60:
            print(nombre, "debe ir a URGENCIAS")
        else:
            print(nombre, "debe ir a consulta PRIORITARIA")

    else:
        # AND si la temperatura es menor a 38
        if temperatura < 38 and sintomas == "no":
            print(nombre, "puede quedarse en CASA")
        else:
            print(nombre, "se recomienda CONSULTA")

# Manejo errores
except ValueError:
    print("Error: Debe ingresar numeros en edad y temperatura")

finally:
    print("\nPrograma finalizado")