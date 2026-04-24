x = None # None es la ausencia de valor
print(x) # None
print(type(x)) # <class 'NoneType'>

# None es un objeto de tipo NoneType
# None es un valor singular, es decir, solo existe una instancia de NoneType
# None es un valor falso en un contexto booleano
if x:
    print("No se ejecuta") # No se ejecuta
else:
    print("Se ejecuta") # Se ejecuta

if x is None:
    print("Es None") # Es None
# Operador ternario
print("Es None" if x is None else "No es None")

# None es diferente a False, 0, "", [], (), {}, set()
print(type("")) # <class 'str'>
print(type(0)) # <class 'int'>
print(type(False)) # <class 'bool'>
print(type([])) # <class 'list'>
print(type(())) # <class 'tuple'>
print(type({})) # <class 'dict'>
print(type(set())) # <class 'set'>