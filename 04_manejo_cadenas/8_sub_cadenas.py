

"""subcadenas en Python

Una subcadena es una parte de una cadena principal,  hay varias maneras de extraer subcadenas en python

Podemos extraer subcadenas, buscarlas, remplazarlas, entre otras operaciones.

- En la extracción cadenas se usa slicing : 
    El slicing o segmentación permite indicar el indice de inicio y el indice final (sin incluir este ultimo)
    Ej.
        subcadena = cadena[inicio:fin]
"""

# Manejo de subcadenas

cadena = "Hola, Mundo"

subcadena_hola = cadena[0:4] #* Obtenemos la subcadena de "Hola" [indice:fin(no se incluye el fin)

print(f"Subcadena de hola : {subcadena_hola}")

subcadena_mundo = cadena[6:10]

"""
    -Para remplazar subcadenas se usa "replace":
        El metodo replace() reemplaza una subcadena por otra dentro de una cadena principal
"""

#! esto en su mayoria se usa con un input (el usuario pone los datos) esto es solo una represtacion de solo se usa

cadena = "Hola Mundo"
nueva_cadena  = cadena.replace('Mundo','a todos') #* Esta linea remplazara (Mundo) por (a todos) cuando se cree un print
print(nueva_cadena)


""""  Extraer subcadenas por separadores:
        la funcion split permite dividir una cadena en una lista de subcadenas basadas en un caracter separador
    Ej
"""
datos = "Juan,30,Cuba"
lista_contacto = datos.split(",")
print(lista_contacto) #* -> esto me dara una lista ["Juan","30","Cuba"]

# Multiplicando cadenas 

cadena = "Hola"

resultado = cadena * 4

print(resultado)

