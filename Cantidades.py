nombres_productos = []
cantidades_stock = []

try:
    limite = int(input("¿Cuántos productos desea registrar?: "))
    
    for i in range(limite):
        nombre = input(f"\nNombre del producto {i+1}: ")
        stock = int(input(f"Cantidad en stock de {nombre}: "))
        
        nombres_productos.append(nombre)
        cantidades_stock.append(stock)

    print("\n--- REPORTE DE INVENTARIO ---")

    for i in range(len(nombres_productos)):
        nombre = nombres_productos[i]
        cantidad = cantidades_stock[i]
        
        if cantidad == 0:
            print(f"CRÍTICO: {nombre} - Solicitar pedido urgente")
        elif cantidad >= 5:
            if cantidad > 20:
                print(f"{nombre}: Stock excelente")
            else:
                print(f"{nombre}: Stock saludable")
        else:
            print(f"{nombre}: Stock bajo (requiere atención)")

    total_productos = len(nombres_productos)
    
    if total_productos > 0:
        suma_total = 0
    
        for i in range(len(cantidades_stock)):
            suma_total += cantidades_stock[i]
    
        promedio = suma_total / total_productos
    
        print("-" * 30)
        print(f"Suma total de stock: {suma_total}")
        print(f"Promedio de stock: {promedio:.2f}")
        
    else:
        print("No se registraron productos.")

except ValueError:
    print("Error: Por favor, ingrese solo números enteros para las cantidades.")