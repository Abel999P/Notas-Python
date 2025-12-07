from decouple import config 
import mysql.connector 


conexion = mysql.connector.connect(
        host=config("HOST_DB"),
        user=config("USER_DB"),
        password=config("DB_ROOT_PASSWORD"),
        database=config("NAME_DB")
        )
cursor = conexion.cursor()

columna = "nombre"

consulta = f"UPDATE personas SET {columna} = %s WHERE id=%s" 

valores = ("Victor2",4)

cursor.execute(consulta,valores)
conexion.commit()

print(f"Fila modificada: {cursor.rowcount}")

cursor.close()
conexion.close()


 
