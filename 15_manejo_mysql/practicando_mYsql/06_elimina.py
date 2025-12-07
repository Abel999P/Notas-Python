from decouple import config
import mysql.connector

conexion = mysql.connector.connect(
    host=config("HOST_DB"),
    user=config("USER_DB"),
    password=config("DB_ROOT_PASSWORD"),
    database=config("NAME_DB")
)

cursor = conexion.cursor()

consulta = "DELETE FROM personas WHERE id = %s"
cursor.execute(consulta, (3, ))

conexion.commit()

print("Filas eliminadas:", cursor.rowcount)

cursor.close()
conexion.close()
