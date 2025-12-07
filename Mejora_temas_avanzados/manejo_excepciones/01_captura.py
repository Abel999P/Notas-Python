
lista1 = [1,2,3]

try:
    print(lista1[4])
except IndexError as e:
    print(f"Error de indice = {e}")
finally:
    print("Cerrando programa ...")

print("separador".center(100,"-"))
"""
    Lanzar Excepciones
"""

try:
    raise TypeError 
except TypeError as e:
    print(f"Error con los tipod de datos... {e}")

"""
    Nuestros errores 
"""

class Err(Exception):
    def __init__(self,valor) -> None:
        print(f"Se couso un error por : {valor}")

TypeError
try:
    raise Err(2)
except Err:
    print("Error escrito")

