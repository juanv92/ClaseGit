lista_maestra = [[], []]

for i in range(3):
    precio = float(input(f"Ingrese el precio {i+1}: "))
    lista_maestra[0].append(precio)

lista_maestra[0].insert(0, "Temporal")
lista_maestra[0].pop(0) 

subtotal = 0

for i in range(len(lista_maestra[0])):
    subtotal += lista_maestra[0][i]


es_estudiante = input("¿Es estudiante? (si/no): ").lower()
descuento = 0

if es_estudiante == "si":
    if subtotal > 50:
        descuento = 0.5 
else:
    
    if subtotal > 50:
        descuento = 0.1  
    else:
        descuento = 0   


total_menos_descuento = subtotal - descuento


print("\n" + "="*20)
print(f"SUBTOTAL: {subtotal}")
print(f"DESCUENTO: {descuento}")
print(f"TOTAL: {total_menos_descuento}")
print("="*20)


lista_maestra[1].append(subtotal)
lista_maestra[1].append(descuento)
lista_maestra[1].append(total_menos_descuento)

print(f"Dato guardado en lista_maestra[1][2] (Total): {lista_maestra[1][2]}")