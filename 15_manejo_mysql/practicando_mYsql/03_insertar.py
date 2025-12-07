from decouple import config 
import mysql.connector 

conexion = mysql.connector.connect(
        host=config("HOST_DB"),
        user=config("USER_DB"),
        password=config("DB_ROOT_PASSWORD"),
        database=config("NAME_DB")
        )

cursor = conexion.cursor()

consulta = "INSERT INTO personas(nombre,apellido,edad) VALUES(%s,%s,%s)"


# Para insertar multiples filas puedes crear una lista de tuplas 
valores = ("Victor","Ramos",46)

cursor.execute(consulta,valores)

conexion.commit()


print(f"Se ha agregado el nuevo regustro a la BD : \n {valores}")

cursor.close()
conexion.close()

