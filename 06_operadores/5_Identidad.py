
"""   
El operador de Identidad: se usa para comparar si dos variables hacen referencia al mismo objeto en memoria, no si su contenido es igual.
Es decir, verifican identidad, no igualdad.

En Python hay dos operadores de identidad:
    -is	(Significa  Es, Ambos objetos son el mismo en memoria)
    -is not	(Significa No es, Los objetos son diferentes en memoria)

Ejemplo:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a == b:", a == b)  # True

print("a is b:", a is b)  # True → mismo objeto

print("a == c:", a == c)  # True → mismo contenido

print("a is c:", a is c)  # False → distinto objeto

# Comparando con None
x = None
print(x is None)    # True
print(x is not None)  # False

# None  

"""
