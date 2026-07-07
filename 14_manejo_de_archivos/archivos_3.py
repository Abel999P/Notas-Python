
# Codigo x para escribir de modo exclusivo  

nombre_archivo = "mi_archivo.txt"

try:
    with open(nombre_archivo,"x") as archivo:
        archivo.write("Escritura en modo esclusivo")
        archivo.write(" Espero te sea util")
    print(f"Se ha creado el archivo : {nombre_archivo}")

except FileExistsError as e:
    print(f"El archivo {nombre_archivo} ya existe")
    print(f"Detalle del error {e}")



