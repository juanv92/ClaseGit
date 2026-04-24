print('Hola "mundo"') # Output: Hola "mundo"
salto_linea = """Hola
mundo"""
print(salto_linea)

# Identificar numero de caracteres de una palabra (metodo len)
palabra = "Parangaricutirimicuaro"
print(len(palabra)) # Output: 22

# Identificar si una palabra esta o no incluida en un texto (metodo in, not in)
texto = "Aprendiendo del curso de fundamentos de Python"
incluida = "curso" in texto # Output: True , es sensible a mayusculas y minusculas
incluida2 = "hola" in texto # Output: False
no_incluida = "mundo" not in texto # Output: True
print(incluida, incluida2, no_incluida)

# Pasar de minusculas a mayusculas (metodo upper) y visiversa (metodo lower)
mayuscula = texto.upper()
minuscula = mayuscula.lower()
print(mayuscula)
print (minuscula)

# Eliminar espacios de un texto (metodo strip)
espacios = "          Este es el texto         "
sin_espacios = espacios.strip()
print(espacios)
print(sin_espacios)