"""
    -Variables locales y globales (scope)

variable = 3  # Esta es una variable GLOBAL, accesible desde cualquier parte del programa.

def funcion():
    global variable  #* Indicamos que dentro de esta función usaremos la variable global 'variable', no una local (funciones).
    variable = 0     #* Modificamos el valor de la variable global.
    print(variable)  #* Imprime el valor actual de la variable (ahora es 0).

funcion()           #* Llamamos a la función, por lo tanto, imprime 0.
print(variable)     #* Fuera de la función, imprimimos la variable global, que también cambió a 0.

"""

print("Variables locales y globales (scope)".center(100,"-"))

variable = 3

def funcion():
    variable = 0
    return variable

print(funcion()) #*-> 0
print(variable) #* -> 3

print(f"Ejemplo de como funciona global".center(100,"-"))

variable1 = 3 #* -> 3

print(variable1) #* -> 3

def funcion():
    global variable1     
    variable1 = 0
    return variable1

print(funcion()) #* -> 0
print(variable1) #* -> 0
