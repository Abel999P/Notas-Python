
def lower(elementos):return elementos.lower()

lista1 = ["Maria","Juan","Si"]

print(list(map(lower,lista1)))



def saludar(idioma):
    def saludar_es():
        print("Hola")
    def saludar_usa():
        print("Hi")

    funciones_idioma={
            "es":saludar_es,
            "usa":saludar_usa
            }
    return funciones_idioma[idioma]


resultado = saludar("usa")
resultado()

"""
    Programacion funcional reduce 
"""

from functools import reduce 

numero = (1,2,3,4)

def sumar(x,y):
    return x+y 

sumar = reduce(sumar,numero)
print(sumar)
