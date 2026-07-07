nombre_archivo = "mi_archivo.txt"

# Abrir el archivo en modo escritura ("w")
archivo = open(nombre_archivo,"w")
archivo.write("Hola como estas")
archivo.write("\nEstoy agregando informacion al archivo")
archivo.close()

print(f"Se creo el archivo : {nombre_archivo}")



