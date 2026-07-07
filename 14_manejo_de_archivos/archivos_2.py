
"""
Ej 1 

nombre_archivo = "mi_archivo.txt"

archivo = open(nombre_archivo,"w")
archivo.write("Hola como estas")
archivo.write("\nEstoy agregando informacion al archivo")
archivo.close()

print(f"Se creo el archivo : {nombre_archivo}")

"""
nombre_archivo = "mi_archivo.txt"

# El uso de with para evitar usar close  
with open(nombre_archivo,"w") as archivo:
    archivo.write("Hola esta información")
    archivo.write("\nSe esta agregando desde un bloque with")


print(f"Se creo el archivo: {nombre_archivo}")


