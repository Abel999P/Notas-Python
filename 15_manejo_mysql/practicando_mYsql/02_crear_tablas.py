from decouple import config 
import mysql.connector


conexion = mysql.connector.connect(
        host=config("HOST_DB"),
        user=config("USER_DB"),
        password=config("DB_ROOT_PASSWORD"),
        database=config("NAME_DB")
        )

cursor = conexion.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS personas(
               id INT PRIMARY KEY AUTO_INCREMENT,
               nombre VARCHAR(100),
               apellido VARCHAR(100),
               edad INT
               )
               """)

print("Tabla creada correctamente")

cursor.close()
conexion.close()

