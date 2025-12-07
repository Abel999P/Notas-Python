
"""Formateo de Cadenas 

Python ofrece varias maneras de formatear cadenas, que incluyen la capacidad de conatenar texto, variables e incluso
dar otro tipo de formateo, como por ejemplo indicar el numero de decimales a utilizar en el formato.

- F-string (python 3.6 en adelante): Esta es la opcion mas recomendada, por ser la mas sencilla,rapida y legible
- Metodo format . Es muy versatil y poderoso Permite construir cadenas muy complejas .format 
"""

# Formateo de cadenas 

nombre = "Juan"
edad = 30

#* f-string lo que hace esto es arrojar directamente el contenido de la variable sin ambiar el tipo de dato 
mensaje = f"Hola me llamo {nombre} y tengo {edad} años"
print(mensaje)

#* Metodo format 
mensaje = "Hola me llamo {} y tengo {} años".format(nombre,edad)
print(mensaje)

#* Ejemplo de como usar .2f para ver 2 decimales usando .format
precio = 1234.56789
print("Precio: ${:.2f}".format(precio)) #* -> 2 decimales 
print("Precio redondeado a 4 decimales: {:.4f}".format(precio)) #* 4 decimales
print("Precio con ancho y alineado: {:>10.2f}".format(precio)) #* solo se mostraran 10 numeros y 2 decimales y se mostrara alineado


precio = 45.678
print(f"Izquierda : {precio:<10.2f}") #* esto sirve para poder moer la variable a dierentes posiciones: >^<
print(f"Centrado  : {precio:^10.2f}")
print(f"Derecha   : {precio:>10.2f}")


num = 45.6
precio_formateo = f"{num:-^10.2f}"
print(precio_formateo)


precio_formateo = f"{45.6:-^10.2f}"
print(precio_formateo)

print(f"Con guiones: {num:-^10.2f}")  #* centrado con guiones: -^
print(f"Con ceros: {num:0>10.2f}")    #* derecha con ceros: 0>

