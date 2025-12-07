"""
    -None type 
None type es un tipo de dato que representar la ausencia de datos

Ejemplo:
def saludar(nombre):
    print(f"Hola {nombre}")
valor = saludar("Lucas")
print(valor)
"""

def saludar(nombre):
    print(f"Hola {nombre}")

# saludar se ejecutara y el valor de la funcion el cual será (nonetype (ningun tipo)) guardara en la variable "valor"
valor = saludar("Lucas")

print(type(valor))  #ejecutara el tipo de valor q tiene la variable, "valor" la cual será "nonetype" ya que en python todos 
                    #los tipos de datos deben deoer un alor y en este caso las variables no tenian ningun tipo de dato que deoler asi que le pusieron por defecto el nonetype
print(valor)

# Pero si ponemos return la funcion devolvera lo que este alado de return y no none que es el dato por defecto 

def suma(num1,num2):
    num1+num2

numero = suma(2,3)
print(numero)


def suma(num1,num2):
    return num1+num2

numero = suma(2,3)
print(numero)

