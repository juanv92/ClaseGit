import mysql.connector

def mostrar_todo_automatico():
    try:
        # Configuración (Asegúrate de poner TU contraseña aquí)
        conexion = mysql.connector.connect(
            host='127.0.0.1', # Cambia 'localhost' por este número
            user='root',
            password='TU_CLAVE_AQUÍ', 
            database='la_colmenita',
            auth_plugin='mysql_native_password'
        )
        
        if conexion.is_connected():
            cursor = conexion.cursor(dictionary=True)
            
            # 1. Mostrar Productos
            print("\n" + "="*40)
            print("📦 INVENTARIO ACTUAL - LA COLMENITA")
            print("="*40)
            cursor.execute("SELECT nombre_producto, marca FROM productos")
            productos = cursor.fetchall()
            
            if not productos:
                print("No hay productos registrados.")
            for p in productos:
                print(f"🔹 {p['nombre_producto']} | Marca: {p['marca']}")

            # 2. Mostrar Clientes
            print("\n" + "="*40)
            print("👥 CLIENTES REGISTRADOS")
            print("="*40)
            cursor.execute("SELECT nombre, apellido FROM clientes")
            clientes = cursor.fetchall()
            
            if not clientes:
                print("No hay clientes en la base de datos.")
            for c in clientes:
                print(f"👤 {c['nombre']} {c['apellido']}")
            
            print("\n" + "="*40)
            print("✅ Fin del reporte.")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()

if __name__ == "__main__":
    mostrar_todo_automatico()