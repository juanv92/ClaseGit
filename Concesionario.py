consecionario = []
carro1 = {
    "Modelo": "Ferrari",
    "Precio": 900000.00,
    "Kilometraje": 0,
}
consecionario.append(carro1)

carro2 = {
    "Modelo": "Lamborgini",
    "Precio": 800000.00,
    "Kilometraje": 0,
}
consecionario.append(carro2)
print(carro1.get("Modelo"))
print(carro2.get("Modelo"))