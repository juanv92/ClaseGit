mi_variable = 234
mi_variable = int(input("ingrese un numero\n"))
# int() Texto a numeros

if mi_variable <= 50 and mi_variable > 40:
    print("Excelente")
elif mi_variable <= 40 and mi_variable > 35:
    print("Sobresaliente")
elif mi_variable >= 30 and mi_variable <= 35:
    print("Aceptable")
elif mi_variable <= 29 and mi_variable >= 0:
     print("Reprobo")
else:
    print("Numero no es valido")