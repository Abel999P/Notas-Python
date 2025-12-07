from decouple import config 
from mysql.connector import pooling 
from mysql.connector import Error


class Conexion:

    POOL_SIZE = 5
    POOL_NAME="zona_fit_pool"
    pool = None 

    @classmethod 
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool 
            try:

                cls.pool = pooling.MySQLConnectionPool(
                        pool_name=cls.POOL_NAME,
                        pool_size=cls.POOL_SIZE,
                        host=config("HOST_DB"),
                        port=config("DB_PORT"),
                        database=config("NAME_DB"),
                        user=config("USER_DB"),
                        password=config("DB_ROOT_PASSWORD")
                        )
                return cls.pool 
            except Error as e:
                print(f"Error al obtener pool: {e}")
        else:
            return cls.pool 

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()


    @classmethod
    def liberar_conexion(cls,conexion):
        conexion.close()
        print("cerrando conexion")


if __name__=="__main__":
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')

