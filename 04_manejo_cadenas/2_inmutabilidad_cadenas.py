
"""PARA MAS TARDE"""


"""INMUTABILIDAD DE UNA CADENA
Una vez que se crea una cadena los caracteres dentro de ella se uelen inmutables, no pueden ser modificados.
si deseamos modificar una cadena, entonces tenemos que crear una nueva cadena. """

# Inmutabilidad en cadenas 

cadena1 = "Hola Mundo"

# Si tratamos de modificar una cadena dara como resultado el error
# TypeError: 'str' object does not support item assignment
#cadena1[0] = "M"

variable1 = "cadena1"
variable2 = variable1
variable1= "cadena modificada"
print(variable2)

variable1 = "cadena1"
variable2 = "cadena modificada"


#   python por defecto tiene un recolector de basura (elimina un valor si no hay ningun puntero apuntando al valor)
# para no duplicar valores python usa punteros para usar elmismo valor para variables qeu tienen el mismo valor 
# siempre cuando un valor tenga una variable que los este referenciando podran ser usados
#cadena2 = cadena1 
#cadena1 = "Otra cadena"
#
#print(cadena1)
#print(cadena2)
