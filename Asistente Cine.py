# Asistente Cine

print("--- BIENVENIDO AL CINE ---")

try:
    # Datos de entrada
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    dinero = float(input("¿Cuánto dinero tiene disponible?: "))
    es_socio = input("¿Tiene tarjeta de socio? (si/no): ").upper()

    print("\n--- Resultado de su visita ---\n")

    # Lógica de Películas (Basada en Edad)
    if edad >= 18:
        print(f"{nombre}, puede ver películas: Acción R, Terror o Documentales.")
    elif edad >= 12:
        print(f"{nombre}, puede ver películas: Animación o Acción PG-13.")
    else:
        print(f"{nombre}, solo puede ver películas: Infantiles.")

    # Lógica de Combos (Basada en Dinero y Membresía)
    # Si es socio o tiene mucho dinero, accede a mejores combos
    # Uso de OR para presupuesto alto o socio
    if dinero >= 50 or es_socio == "si":
        
        # Anidado: Detalles del beneficio
        if es_socio == "si" and dinero < 20:
            print("Recomendación: Combo Socio (Palomitas pequeñas) por su fidelidad.")
        elif dinero >= 50:
            print("Recomendación: Combo Grande con Nachos y Bebida XL.")
        else:
            print("Recomendación: Combo Dúo Especial.")

    else:
        # Uso de AND para presupuesto ajustado
        if dinero < 15 and es_socio == "no":
            print("Recomendación: Solo puede comprar una bebida o snacks individuales.")
        else:
            print("Recomendación: Combo Básico Personal.")

# Manejo de errores
except ValueError:
    print("Error: Por favor, ingrese números válidos para edad y dinero.")

finally:
    print("\n¡Disfrute la función!")