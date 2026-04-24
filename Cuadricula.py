cantidad = int(input("Ingrese el tamaño de la cuadricula"))

cuadricula = []

for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)  # Aquí puedes poner el valor que quieras
    cuadricula.append(fila)

# Mostrar el resultado de forma bonita
for fila in cuadricula:
    print(fila)