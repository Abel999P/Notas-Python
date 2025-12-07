

"""Metodos de cadenas 

Las cadenas en Python vienen con una serie de metodos utiles que facilitan su manipulacion Por ejemplo:
    .upper() -> Cambia las letras a mayusculas
    .lower() -> Cambia las letras a minusculas
    .strip() -> Elimina espacios en blanco al inicio y al final de la cadena 
"""

# Hay muchos metodos mas 

cadena1 = "Hola Mundo"
print(f"Cadena original {cadena1}")

#*Con variables utilizando mas espacio
cadena1=cadena1.upper()
print(f"Cadena con upper {cadena1}")

#*Esto es sin variables utilizando menos espacio
print(f"Cadena con upper: {cadena1.upper()}")
# Esto trasformara todos los caracteres 
print(f"Cadena con lower {cadena1.lower()}")

cadena2 = "  Juan Perez "
print(f"Cadena con espacios :\n{cadena2}")
print(f"Cadena con espacios con strip \n{cadena2.strip()}")

