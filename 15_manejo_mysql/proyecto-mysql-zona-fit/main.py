from decouple import config 
import mysql.connector 



def crear_zona_fit_db():
    try:
        conexion = mysql.connector.connect(
            host=config("HOST_DB"),
            user=config("USER_DB"),
            password=config("DB_ROOT_PASSWORD")
        )

        cursor = conexion.cursor()
        
        consulta = "CREATE DATABASE IF NOT EXISTS zona_fit_db"
        cursor.execute(consulta)
    
        cursor.close()
        conexion.close()
    except mysql.connector.Error as e:
        print(f"Error en MYSQL: {e}")


def crear_tabla_cliente():
    try:
        conexion = mysql.connector.connect(
            host=config("HOST_DB"),
            user=config("USER_DB"),
            password=config("DB_ROOT_PASSWORD"),
            database=config("NAME_DB") 
            )  
        cursor = conexion.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
                       id INT NOT NULL AUTO_INCREMENT,
                       nombre VARCHAR(100) NULL,
                       apellido VARCHAR(100) NULL,
                       membresia INT NULL,
                       PRIMARY KEY(id),
                       UNIQUE INDEX membresia_UNIQUE(membresia ASC) VISIBLE)""")

        cursor.close()
        conexion.close()

    except mysql.connector.Error as e:
        print(f"Error en MYSQL: {e}")




if __name__=="__main__":
    crear_zona_fit_db()
    crear_tabla_cliente()

