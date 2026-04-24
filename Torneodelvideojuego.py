try:
    estatorneo = input("Torneo de video juegos").upper()

    if estatorneo == "SI":
       print("Bienvenido")
    elif estatorneo == "NO":
       edad = int(input("Ingrese su edad:\n"))
       if edad >= 18 and edad < 50:
            puntaje = int(input("Ingrese su puntaje:\n"))
            if puntaje >= 100:
               print("Bienvenido")
            else:
               print("No tienes el puntaje necesario")   
       else:
            print("Edad no permitida")   
    else:
        raise AssertionError  
       
except ValueError:
    print("Estas ingresando texto")
except:
    print("Valor incorrecto")
finally:   
    print("Finalizo el programa")         