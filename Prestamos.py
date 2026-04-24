print("----INICIA PROGRAMA-----")

edad_cliente = int(input("Ingrese su edad: \n"))
ingresos = float(input("ingrese sus ingresos: \n"))

fiador = input("tiene usted un fiador?: (SI/NO)\n")
reportado = input("Esta reportado?: (SI/NO)\n").upper() == "SI"

if fiador.upper() =="SI":
    fiador = True
elif fiador.upper() =="NO":
    fiador = False
else:
    print("Valor no valido")

edad =(edad_cliente >= 18 and edad_cliente < 75)
es_solvente = (ingresos >= 2000000 or fiador)

historial = not reportado # Si coloco un NO historial sera falso
credito_estado = edad and es_solvente and historial 

mensaje = ""
if credito_estado:
    mensaje = "Felicitaciones."
else:
    mensaje = "Lo sentimos."


print("----Resultado----")
print("Edad valida" , edad)
print("Es solvente" , es_solvente)
print("Su historial crediticio limpio: ", historial)
print("-----------")
print(f"Se aprobo su credito?: {credito_estado} {mensaje}")
