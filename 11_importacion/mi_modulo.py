
variable = "esta variable esta en el archivo mi_modulo.py"

def funcion():
    return "esta funcion esta en el archivo mi_modulo.py"

class MI_clase():
    def __init__(self,nombre):
        self.nombre = nombre
    def saludar(self):
        print(f"Hola yo soy {self.nombre}")

if __name__ == "__main__":
    print(f"Este main es del modulo mi_modulo.py {__name__}")