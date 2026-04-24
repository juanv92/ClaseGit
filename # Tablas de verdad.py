# Tablas de verdad

A = False
B = False

print(A and (A == B) or B)

print("-----Logica con numeros-----")

numero1 = 5
numero2 = 10

if numero1 < numero2 and (7 >= 4) and (True and False):
    resultado = 7 > 4
    print(resultado)
elif 7 > 7 or -13 < -3:
    print("ELIF")