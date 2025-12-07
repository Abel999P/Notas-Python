
class Cliente:
    def __init__(self,id=None,nombre=None,apellido=None,membresia=None) -> None:
        self.id = id 
        self.nombre = nombre 
        self.apellido = apellido 
        self.membresia = membresia 

    def __str__(self) -> str:
        return f"ID:{self.id}-Nombre:{self.nombre}-Apellido:{self.apellido}-Membresia:{self.membresia}"
     
