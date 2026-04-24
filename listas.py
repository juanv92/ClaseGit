inventario = [1, 2, "Hola", True, 0.9] # [] es para leer una posicion
print(inventario[3]) # True
inventario.append("Mundo") #[1, 2, "Hola", True, 0.9, "Mundo"] #agrega un dato a la lista
print(inventario)
inventario.insert(1, "Uva") #agrega al elemento en una posicion especifica
print(inventario)
inventario.pop() #Elimina el ultimo
inventario.pop(1)
print(inventario)
inventario.remove("Hola") #elimina un elemento en especifico entre las primeras posiciones
print(inventario)
inventario2 = ["Nada", "NADA","nada", "Nada"]
inventario2.remove("Nada")
print(inventario2)
inventario3 = [1, 3, 65, 12, 46, 1, 3, 5] #si los organiza
inventario3.sort ()
print(inventario3)
inventario3[0] = "Hello",
inventario3[3] = "Texto"
print(inventario3)
prueba = inventario3[0:5:2]
print(prueba)

inventario4 = []
for i in range(0,20): #0 es donde inicia el 20 donde termina
    inventario4.append(i)
#print(inventario4[0:20:2]) #0 es donde inicia el 20 donde termina 2 salto
# for recorre la lista
# la i es una variable y es el valor que toma de una lista
# contador
longitud = len(inventario2)
contador = 0
for i in inventario2:
    if contador < longitud:
        print(inventario2[contador])
        contador += 3

lista = [["Hola","Mundo"],1,2,3, ["Mundo"]]        
print(lista[0][1]) # con el doble[] puedo ingresar a una lista dentro de otra lista
#len y es lo mismo que el size el range es rango del for
for i in range (len(lista)):
    print(lista[i])
    