from conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECIONAR = "SELECT * FROM clientes ORDER BY id;"
    INSERTAR = "INSERT INTO clientes(nombre,apellido,membresia) VALUES(%s,%s,%s);"
    ACTUALIZAR = "UPDATE clientes SET nombre=%s,apellido=%s,membresia=%s WHERE id_cliente=%s;"
    ELIMINAR = "DELETE FROM clientes WHERE id_cliente=%s;"

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes

        except Exception as e:
            print(f"Error al seleccionar clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == "__main__":
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)
