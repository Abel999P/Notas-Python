"""
Todos estos bucles se pueden combinar con las estructuras de datos para recorrer su contenido:

cadenas "str"
listas [list]
tuplas (tuple)
conjuntos {set}
diccionarios {dict}


                                    Bucle for
                                    
Sintaxis:
    
    for variable in iterable:
        # Código que se ejecuta en cada vuelta del bucle 

Ejemplo:
for fruta in ["manzana", "banana", "cereza"]:
    print("Me gusta la", fruta)
Explicación:
iterable es la lista ["manzana", "banana", "cereza"].
En cada iteración, fruta toma un valor distinto: primero "manzana", luego "banana", luego "cereza".
El bloque se ejecuta 3 veces (una por cada elemento).
"""

#!existen varias formas de escribir un blucle


#*designando y poniendo el nombre de la variable directamente en el bucle

frutas = ["manzana", "banana", "cereza"]

for x in frutas:
    print(f"me gusta la {x}")   #* se pone la variable "x" que tomara los valores de la variable pricipal 


#*poniendo directamente los "valores " que quiero que se ejecuten

for x in ["cabello", "uñas", "pestañas"]:
    print(f"Me gusta tu {x} baby")         
    



"""
                                    Bucle while
Sintaxis:
    while condicion:
        # Código que se ejecuta ¡¡mientras!! la condición sea True
Ejemplo:
contador = 0
while contador < 3:
    print("Contador =", contador)
    contador += 1

Explicación:
La condición es contador < 3.
Inicia con contador = 0. Mientras sea menor que 3, ejecuta el bloque y luego incrementa.
Cuando contador llega a 3, la condición es False y se sale del bucle.
"""
#contador te falta la variable contador !!!! 
contador= 0
while contador < 3:
    print("Contador =", contador)
    contador += 1


"""
                Herramientas extra: break, continue, else en bucles 

-break
Sale de inmediato del bucle cuando se ejecuta.
Ejemplo:
for x in range(10):
    if x == 5:
        break
    print(x)
# Imprime 0,1,2,3,4 y luego se detiene.
"""

for X in range(10):#es un bunlce que dice en español para x que tiene un valor del 1 al 9
    if X == 5:#oseea que aca cuenta es 1 2 3 4 y cuando lleve al 5 que no lo vale, se cierra e
        break
    print(X)


frutas1 = ["manzana", "banana", "cereza","peras"]

for x in frutas1:#es un bunlce que dice en español para x que esta en fruta1
    if x == "cereza":# si x que esta almacenando la variable fruta1  tiene un contenido que se llame igual a cereza
        break# cierra el buncle
    print(f"me gusta la {x}")  #


"""
                -continue
Salta solo esta iteración y continúa con la siguiente.
Ejemplo:
for X in range(5):
    if X == 2:
        continue
    print(X)
# Imprime 0,1,3,4 (salta el 2)
"""

for variableX in range(5):
    if variableX == 2:
        continue
    print(variableX)


"""
            -else en bucles
Se ejecuta después del bucle si no se ha salido con break.
Ejemplo:
intentos = 3
while intentos > 0:
    if input(">>> Escriba la contraseña:") == "BitBoss":
        print("¡Correcta!")
        break
    intentos = intentos - 1
    print("Contraseña incorrecta")
else:
    print("Se te acabaron los intentos :(") # Si el bucle no salio con break se ejecutara el else
"""

intentos = 3
while intentos > 0:
    if input(">>> Escriba la contraseña:") == "BitBoss":
        print("¡Correcta!")
        break
    intentos = intentos - 1
    print(f"Contraseña incorrecta te quedan {intentos} intentos")
else:
    print("Se te acabaron los intentos :(") # Si el bucle no salio con break se ejecutara el else

