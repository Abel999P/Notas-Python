"""
Sistema de Empleados
Crea un programa para solicitar la
información de un empleado, introduciendo
los datos por consola para lugo imprimirlos.

	• Nombre Empleado
	• Edad del Empleado (convertir a entero)
	• Salario del Empleado (convertir a flotante)
	• Es jefe de departamento (si / No)
"""  

print("Sistema de Empleados".center(100))

nombre=  input("cual es tu nombre? ")
edad = int (input("que edad tienes? "))
salario = int (input("cual es tu salario? "))
jefe = input("Eres jefe de departamento : ")

if jefe.lower() == "si":
	pass
elif jefe.lower() == "no":
	pass
else:
	jefe = "Ingresaste un valor incorrecto"
    

print(f"Estos son tus datos ".center(100,"-"))
print(f"""
Nombre : {nombre}
Edad : {edad}
Salario : {salario}
Jefe de departamento : {jefe} 
""")



"""  
Receta de Cocina
Crear un programa para solicitar algunos valores importantes
para una receta de cocina.

Los valores que debe introducir el
usuario son :

	• Nombre de la Receta
	• Ingredientes
	• Tiempo de preparación (en minutos)
	• Dificultad ("Facil, Media, Alta")
	por ultimo mandar a imprimir la reseta usando fstring
""" 

print("Receta de Cocina".center(100))
Nombre_Receta = input("Nombre de la Receta ")
Ingredientes = input("Ingredientes ").strip(",")
Tiempo_de_preparación = int(input("Ingresa el tiempo de preparación en minutos "))
Dificultad = input("Dificultad - Facil, Media, Alta ")

# No tenemos dos si no tres 
if Dificultad.lower() == "facil":
	pass 
elif Dificultad.lower() == "media":
	pass
elif Dificultad.lower() == "alta":
	pass
else:
	Dificultad = "Pon algo correcto pendejo XD"

print(f"""
Nombre_Receta:  {Nombre_Receta}
Ingredientes: {Ingredientes}
Tiempo_de_preparación:{Tiempo_de_preparación}
Dificultad:{Dificultad}
""")


