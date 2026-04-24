v = True
f = False

print (v)
print (f)

#otra forma de obtener un boleano es con una comparacion
print (10 > 5) #esto es verdadero
print (50 < 10) #esto es falso

print (type(v)) #esto nos dice el tipo de dato de v

#podemos castear un boleano y dependiendo de si tiene un valor o no, sera verdadero o falso

print (bool("hola")) 
print (bool("")) 

#true

print (bool("verdadero"))
print (bool(456))
print (bool(["Pan", "Pizza", "Pera"]))

#false

print (bool(""))
print (bool(0))
print (bool([])) #es una lista vacia, por lo tanto es falso
print (bool(None)) #es un valor nulo, por lo tanto es falso

#saber que tipo de variable es con un booleano

j = 10
print (isinstance(j, int)) #esto es verdadero porque j es un entero

k = 5.7
print (isinstance(k, complex)) #esto es falso porque k no es un numero complejo