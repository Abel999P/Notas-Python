
"""Operadores Logicos: se utilizan para realizar operaciones logicas con valores booleanos

-Operador logico AND (multiplicacion) : Devuelve True si ambos operaciones son verdaderas True

#!FALSE = 0  TRUE = 1

#*AND (MULTIPLICACION)

True AND True   = True
False AND False = False
False AND True  = False
True AND False  = False
"""



yo  = "me amas"
ella = "No te amo"
amante= "me amas"
#   False          True
if yo == 1 and ella == "No te amo":
    print("eres un puto migajero")

#       False                   False
elif yo == "No te amo" and ella == "me amas":
    print("Puto zigma XD")

#
elif yo == "me amas" and ella == "me amas":
    print("que pendejos son los dos")


elif yo == "me amas" and ella=="te veo como amigo":
    print("Frens zone")
    

else:
    print("No tienen preguntas ni respuesta ninguno de estos pendejos")


edad1 = input("dime tu edad: ")
edad = int(edad1)
nombre = "agustin"

if edad <= 18 and nombre == "agustin":
    print("no eres agustin")

elif edad >= 20 and nombre == "agustin":
    print("podrias ser agustin")

else:
    print("si eres agustin")




"""        
-Operador logico OR


#*OR (SUMA)

False OR True  = True
True OR False  = True
True OR True   = True
False OR False = False

"""






"""
-Operador logico not : Invierte el valor del operador es un operador unario al solo requerir un operador


#*NOT (SUMA)


not True  = False
not False = True
    
"""

