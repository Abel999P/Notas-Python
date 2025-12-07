
"""
    -Return (corta el flujo de ejecucion de la funcion)

"""

print("para que sirve return".center(100,"-"))

def imprimir_cosas():
    print("Primer print de la ejecucion")
    return 
    # este print no se ejecutara por que return termina la funcion 
    print("Segundo print de la ejecucion")

imprimir_cosas()



"""
    -Los valores(pueden ser cualquier tipo de dato) que estan al lado de la palabra 
    clave return se almacenara y se devolveran en tuplas 
"""

def funcion():
    return 1, 2, 3 # Devuelve tres valores y los almacenara en una tupla


valor = funcion()  # ejecutamos la funcion y la guardamos dentro de una variable
print(f"{type(valor)} = {valor}")  # type(valor) mostrará <class 'tuple'>  = {valor } mostrara (1,2,3)

# Desempaquetado de tuplas
#Python es inteligente y si quieres definir la misma cantidad que tiene la tupla en variables
#se asignara un valor por variable 
# (1,2,3) a=1 ,b=2 , c=3
a, b, c = funcion()  # Asignamos cada elemento de la tupla a una variable diferente
print(f"valor 1= {a}, valor 2= {b}, valor 3={c}")  # Mostramos los valores individuales
print(f"{type(a)}") # Ahora que los valores seran un tipo de dato y no una tupla 
