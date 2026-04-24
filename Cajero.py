print("Bienvenido al Banco")

saldo = 1000000.0
ejecutando = True

while ejecutando:
    print("\n----MENU PRINCIPAL---")
    print(f"Saldo actual: ${saldo}")
    print("1. Retirar")
    print("2. Consignar")
    print("3. Salir")
    
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        retiro = float(input("Monto a retirar: "))
        
        if retiro > saldo:
            print("Saldo insuficiente")
        elif retiro <= 0:
            print("Monto no valido")
        else:
            saldo -= retiro
            print("Retiro exitoso")
            
    elif opcion == "2":
        deposito = float(input("Monto a consignar: "))
        
        if deposito > 0:
            saldo += deposito
            print("Consignacion exitosa.")
        else:
            print("Monto invalido.")
            
    elif opcion == "3":
        print("Cerrando sesion....")
        ejecutando = False
        
    else:
        print("Opcion invalida")