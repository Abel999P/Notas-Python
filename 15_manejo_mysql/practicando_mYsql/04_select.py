from decouple import config 
import mysql.connector 

# Crear con la base de datos 
conexion = mysql.connector.connect(
        host=config("HOST_DB"),
        user=config("USER_DB"),
        password=config("DB_ROOT_PASSWORD"),
        database=config("NAME_DB")
        )
# Crear un cursor para poder ejecutar sentencias sql
cursor = conexion.cursor()

# Ejecutar una sentencia select 
consulta = "SELECT * FROM personas"
cursor.execute(consulta)

# Obtener los resultados de la consulta 
resultados = cursor.fetchall()

# Imprimir los resultados 
for fila in resultados:
    print(fila)

#Cerrar el cursosr y la conexion 
cursor.close()
conexion.close()


