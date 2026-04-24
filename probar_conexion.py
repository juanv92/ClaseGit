import mysql.connector
from mysql.connector import Error

def diagnostico_colmenita():
    try:
        # Intentamos la conexión con tus datos de local
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='la_colmenita' # Nombre de tu DB
        )

        if conexion.is_connected():
            info_servidor = conexion.get_server_info()
            print(f"✅ Conexión exitosa. Versión de MySQL: {info_servidor}")
            
            cursor = conexion.cursor()
            cursor.execute("SHOW TABLES;")
            tablas = cursor.fetchall()
            
            print("\nTablas encontradas en 'la_colmenita':")
            for t in tablas:
                print(f"- {t[0]}")

    except Error as e:
        print(f"❌ Error al conectar: {e}")
    
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()
            print("\nConexión cerrada correctamente.")

if __name__ == "__main__":
    diagnostico_colmenita()