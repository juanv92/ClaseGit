print("------INICIO PROGRAMA-------")

promedio = float(input("Ingrese un promedio\n"))
deporte = input("Realiza algun deporte: (SI/NO)\n").upper()== "SI"


""" if

"""

if deporte == "SI":
    depote = True
elif deporte == "NO":
     deporte = False
else:
     print("Valor no valido")

gana_beca = (promedio >= 4.5) \
    or (promedio >= 4.0 and deporte)

print(f"El estudiante gano la beca?: {gana_beca}.")


