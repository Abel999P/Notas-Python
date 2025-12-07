


"""
-Operadores de Asignacion se utilizan para asignar valores a variables
-sintxis operador asignacion

#* variable = valor
    
en python tambien tenemos la asignacion multiple, lo que nos permite asignar valores a varias variables
en una sola linea de codigo generando que el codigo sea mas compacto y facil de leer
-sintaxis operador asignacion multiple"""

#* variable1 , variable2 , varable3 = valor1 , valor2 , valor3

""" 
operadores de asignacion compuesto combinan una operacion aritmetica con una asignacion, haciendo las 
operaciones mas conscisas.

#* variables1 = variable1 + 8       hacemos esto mas rapido   variable1 =+ 8

-Los operadores pueden ser 
        +=  ->  
        -=  ->
        *=  ->
        /=  ->
        //= ->    
        %=  -> 
"""
#ejemplos:

num1 , num2 , num3 , num4 , num5 , num6 = 2 , 2 , 2 , 2 , 2 , 2   

num1 +=  4
print(num1)

num2 -=  4
print(num2)

num3 *=  4
print(num3)

num4 /= 4
print(num4)

num5 //= 4
print(num5)

num6 %= 4
print(num6)


"""
type() — es para saber el tipo de dato
Puedes usar type() para ver si un valor es int, float, str, etc.
ejemplo:
"""
suma = 3+3
division = 10/2

print("Tipo de 'suma':", type(suma))
print("Tipo de 'división':", type(division))
