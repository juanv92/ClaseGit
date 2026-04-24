resultado = 0

numero1 = int(input("ingrese un numero\n"))
numero2 = int(input("ingrese otro numero\n"))

#resultado = numero1 + numero2
parametro = None
'''
Comentario
'''
mensaje = """"
     Por favor ingrese la operacion a realizar:
     +) Sumar
     -) Restar
     /) Dividir
     *) Multiplicar\n
"""
parametro = input(mensaje)

if parametro == "+":
    resultado = numero1 + numero2
    print(resultado)
elif parametro == "-":
    resultado = numero1 - numero2
    print(resultado)
elif parametro == "/":
    resultado = numero1 / numero2
    print(resultado)
elif parametro == "*":
    resultado = numero1 * numero2
    print(resultado)
else:
    print("No valido")
    print(resultado)