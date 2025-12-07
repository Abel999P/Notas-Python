

"""Obtener el largo de una Cadena 
Para obtener la longitud de una cadena, utilizamos la funcion incorporada len()

La funcion len funciona con varios tipos de datos incluyen cadenas,listas,etc

Cuando se calcula el largo de una cadena se toman en cuenta todos los caracteres de esta, incluyendo espacios en 
blanco, caracteres especiales, etc.

"""

cadena = "Hola# Mundo !"
largo_cadena = len(cadena)

print(f"El largo de la cadena es de {largo_cadena}")


#* cuando estabamos iendo esto nos dimos cuenta de que al parecer la uncion para encontrar el largo de una cadena 
#* solo cuenta el largo de lo que se va a ejecutar en el terminal no en si de lo que escribimos en la cadena
#* EJEMPLO:

precio_formateo = f"{54.6:-^10.2f}"
largo_precio = len(precio_formateo)
print(precio_formateo)

print(f"El largo de la cadena es de format{largo_precio}")


