"""
    Cuando creamos una funcion podemos poner valores por defecto 
    para abordar si no se pasan argumentos al ejecutar la funcion

    -Orden de parametros con(key arguments)
    cuando queremos llamar a la funcion para ejecutarse
    podemos definir el orden en el que los valores de los argumentos 
    serán ingresados a la funcion para ejecutarce   
    
"""

print("Orden de parametros con(key arguments)".center(100,"-"))

def resta(num_1=1,num_2=1):# Podemos definir argumentos por defecto y alterarlos posteriormene
    return num_1 - num_2

print(resta())
print(resta(5,3))   # -> argumentos alterados 2
print(resta(3,5))   # -> argumentos alterados -2

#en esta linea usamos key arguments
# -> modificamos la posicion de los argumentos para cambiar el resultado final a -2
print(resta(num_2=5,num_1=3))

