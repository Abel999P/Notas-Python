
"""
-Operadores de Membresia: se usan para comprobar si un valor o elemento se encuentra dentro (o no) 
de una secuencia o colección como:

cadenas "str"
listas [list]
tuplas (tuple)
conjuntos {set}
diccionarios {dict}


Ejemplo:

cadena = "Python es divertido"
lista = [1, 2, 3, 4]
conjunto = {"a", "b", "c"}
diccionario = {"x": 10, "y": 20}

print("diver" in cadena)            # True (subcadena)
print(3 in lista)                   # True
print("d" in conjunto)              # False
print("x" in diccionario)           # True (clave)
print(10 in diccionario.values())   # True (valor)

"""