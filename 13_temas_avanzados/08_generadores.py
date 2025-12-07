
"""
Los generadores en Python son una forma sencilla y poderosa de crear iteradores.Permiten generar una secuencia de valores sobre la marcha,de manera eficiente y sin necesidad de 
almacenar todos los valores en la memoria 

Hay dos formas principales de crear generadores en PYthon

Funciones generadores:Estas son funciones que contiene una o más expreciones'yield' , en lugar de 'return'.Cuando se llama a una función generadora,esta devuelve un objeto
generador que puede ser iterado para obtener los valores generados.

"""


def generador (maximo):
    contador = 0
    while contador < maximo:
        yield contador 
        contador += 1

# Creamos un generador 
var_generador = generador(5)

# Iteramos sobre el generador 
for valor in var_generador:
    print(valor)




