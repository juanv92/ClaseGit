import mysql.connector
from mysql.connector import Error

# 1. Función única para gestionar la conexión
def obtener_conexion():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='la_colmenita'
        )
    except Error as e:
        print(f"Error crítico de conexión: {e}")
        return None

# 2. Función para mostrar datos
def visualizar_datos_ferreteria():
    conexion = obtener_conexion()
    if conexion and conexion.is_connected():
        try:
            cursor = conexion.cursor(dictionary=True)
            
            # Consulta de productos
            query_prod = """
                SELECT p.id_producto, p.nombre_producto, p.marca, c.nombre_categoria 
                FROM productos p
                JOIN categorias c ON p.id_categoria = c.id_categoria
            """
            cursor.execute(query_prod)
            print("\n--- INVENTARIO DE LA COLMENITA ---")
            for prod in cursor.fetchall():
                print(f"{prod['id_producto']} | {prod['nombre_producto']} | {prod['marca']}")

            # Consulta de clientes
            cursor.execute("SELECT nombre, apellido, correo FROM clientes")
            print("\n--- LISTADO DE CLIENTES ---")
            for cli in cursor.fetchall():
                print(f"{cli['nombre']} {cli['apellido']} - {cli['correo']}")
                
        finally:
            cursor.close()
            conexion.close()

# 3. Función para registrar datos
def registrar_cliente(nombre, apellido, telefono, correo, mensaje):
    conexion = obtener_conexion()
    if conexion and conexion.is_connected():
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO clientes (nombre, apellido, telefono, correo, mensaje) VALUES (%s, %s, %s, %s, %s)"
            valores = (nombre, apellido, telefono, correo, mensaje)
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"¡Cliente {nombre} registrado con éxito!")
        except Error as e:
            print(f"Error al insertar: {e}")
        finally:
            cursor.close()
            conexion.close()

# 4. Bloque de ejecución principal (SIEMPRE AL FINAL)
if __name__ == "__main__":
    # Primero visualizamos lo que hay
    visualizar_datos_ferreteria()
    
    # Ejemplo de uso de la función de registro
    # registrar_cliente("Juan", "Perez", "3001234567", "juan@correo.com", "Interesado en herramientas")    