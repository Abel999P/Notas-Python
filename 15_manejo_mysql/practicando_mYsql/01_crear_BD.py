
import mysql.connector 
from decouple import config 

conexion = mysql.connector.connect(
        host=config("HOST_DB"),
        user=config("USER_DB"),
        password=config("DB_ROOT_PASSWORD")
        )

cursor = conexion.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS personas")

print("Base de datos creada")

cursor.close()
conexion.close()

