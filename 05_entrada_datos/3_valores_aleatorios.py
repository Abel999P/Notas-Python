"""

                    Generar valoves aleatorios
modulos:
    un modulo son funciones pre fabricadas por los creadores del lenguaje de programacion o modulos
    generados por la comunidad hay algunos mas pesados que otros, en esta ocasion veremos el modulo 
    'random'(mas adelante vamos a generar nuestros modulos y ver donde se alojan los modulos de python)
    
Sintaxis de como importar un modulo :

    from (modulo) import (el nombre de la funcion)  -  from random import (el nombre de la funcion)



La función randint(), que es parte de módulo 'random', nos permite generar números aleatorios

    randint (a, b) -> devuelve un numero entre a y b, esta funcion puede devolver tanto a como b.

Es necesario importar en primer lugar el módulo "random" antes de usarla función "randint"

Sintaxis de como importar la funcion "randing" :

    from (modulo) import (el nombre de la funcion)  -  from random import randing
    
    
    existen mas tipos de funciones dependiendo del modulo que elijamos como por ejemplo: """

    
from random import randrange,choice,choices,randint

    
"""
En este caso, el módulo random no es especialmente pesado, pero hay 
situaciones en las que solo necesitas importar una función o clase específica. 
Usar 

    from (...) import (...) 

permite cargar únicamente lo necesario

Ejemplo de importacion multiple
Traéme solo estas herramientas (randrange, choice, choices y randint) 
de la caja llamada random, porque son las únicas que voy a usar
Sintaxis:
    from random import randrange,choice,choices,randint

    -randrange() → saca un número al azar dentro de un rango.
    -randint() → elige un número entero al azar entre dos valores.
    -choice() → elige un solo elemento al azar de una lista.
    -choices() → elige varios elementos al azar de una lista.

"""



numero = randint(1,10)
print(f"Numero aleatorio entre 1 y 10 : {numero}")

#* Simular un dado de seis caras
dado = randint(1,6)
print(f"Lanzada del dado : {dado}")

