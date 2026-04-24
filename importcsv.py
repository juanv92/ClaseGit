import mysql.connector
import csv

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="colmenita"
)
cursor = db.cursor()

def exportar_a_csv(tabla):
    nombre_archivo = f"reporte_{tabla}.csv"
    cursor.execute(f"SELECT * FROM {tabla}")
    filas = cursor.fetchall()
    columnas = [i[0] for i in cursor.description]

    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(columnas)
            escritor.writerows(filas)
        print(f"\nExportación exitosa: '{nombre_archivo}' generado.")
    except Exception as e:
        print(f"\nError al exportar: {e}")
    except FileNotFoundError:
        print("Error: El archivo 'reporte_.csv' no fue encontrado.")
    except Exception:
        print(f"Error")

def menu_productos():
    while True:
        print("\nTABLA PRODUCTOS")
        print("1. Ver | 2. Agregar | 3. Volver")
        opc = input("Selecciona: ")
        if opc == "1":
            cursor.execute("SELECT * FROM productos")
            for f in cursor.fetchall(): print(f)
        elif opc == "2":
            nom = input("Nombre: "); desc = input("Descripcion: "); mar = input("Marca: ")
            cursor.execute("INSERT INTO productos (nombre_producto, descrip_producto, marca ) VALUES (%s, %s, %s)", (nom, desc, mar))
            db.commit()
        elif opc == "3": break

def menu_categorias():
    while True:
        print("\nTABLA Categorias")
        print("1. Ver | 2. Agregar | 3. Volver")
        opc = input("Selecciona: ")
        if opc == "1":
            cursor.execute("SELECT * FROM categorias")
            for f in cursor.fetchall(): print(f)
        elif opc == "2":
            nombre = input("Nombre: "); apellido = input("apellido: "); tel = input("Teléfono: "); email = input("email: "); mensaje = input("mensaje: ")
            cursor.execute("INSERT INTO categorias (nombre, apellido, telefono, correo, mensaje) VALUES (%s, %s, %s, %s, %s)", (nombre,apellido, tel,email,mensaje ))
            db.commit()
        elif opc == "3": break

while True:
    print("\n--- SISTEMA COLMENITA ---")
    print("1. Gestionar Productos")
    print("2. Gestionar Categorias")
    print("3. Exportar Tabla a CSV")
    print("4. Salir")
    
    principal = input("Elige una opción: ")

    if principal == "1":
        menu_productos()
    elif principal == "2":
        menu_categorias()
    elif principal == "3":
        t = input("¿Qué tabla deseas exportar? (productos/categorias): ")
        exportar_a_csv(t)
    elif principal == "4":
        print("Saliendo...")
        break

db.close()