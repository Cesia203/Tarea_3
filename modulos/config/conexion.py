import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bdysaau7gogcrbesf2xx-mysql.services.clever-cloud.com',
            user='unhgpm3iludainnk',
            password='j3RyxGCrK83QxoJReUm2',
            database='j3RyxGCrK83QxoJReUm2',
            port=3306
        )
        if conexion.is_connected():
            print("âœ… ConexiÃ³n establecida")
            return conexion
        else:
            print("âŒ ConexiÃ³n fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"âŒ Error al conectar: {e}")
        return None
