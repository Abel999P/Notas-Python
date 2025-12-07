

"""CONCATENAION DE CADENAS
La concatenacion de cadenas es una operacion que permite combinar dos o mas cadenas para formar una nueva cadena.
En python existen varias formas, vamos a ver varias.

- Uso del operador +: El operador + es el mas directo par concatenar cadenas.
Simplmente tenemos que poner el operador + entre las cadenas que deseamos unir.

Ej. """

concatenacion = "Hola " + "Mundo"
print(concatenacion)

# Ejemplo de la diferencia de concatenar int y string
# Int
num1 = 2
num2 = 3
print(num1+num2) #* -> Esto dara 5

# String
num1 = "2"
num2 = "3"
print(num1+num2) #* -> Esto dara 23

num1 = 2

#! print("Mi numero favorito es el" + num1) -> Esto daria error ya que estoy intentando concatenar un tipo de dato str y un dato int

print("Mi numero faorito es el" + str (num1)) #* -> la transormacion d datos se mostrara en otro documento ENTRADA DE DATOS PRIMERA PARTE 

"""
# Uso de la funcion join: La funcion join nos permite unir tantas cadenas como necesitemos. 
Solo necesitamos pasar cada cadena a concatenar separadas por coma y entre corchetes.

Ej.
"""
cadenaJ = "".join(["Cadena1","Cadena2","Cadena3"])
print(cadenaJ)

