"""
                                     Cuadro de Conversiones (Casting) en Python

La conversion de tipos de datos, tambien 
conocido como casting, es una tecnica 
para manipular datos que no etan en el 
tpo requerido.

Podemos hacer conversiones desde y hacia
distintos tipos de datos 
Ej.

 Tipo de conversión | Función usada | Ejemplo                      | Resultado / Tipo resultante
 ----------------------------------------------------------------------------------------------
 Entero → Flotante   | float()       | float(5)                     | 5.0  (float)
 Entero → Cadena     | str()         | str(5)                       | "5"  (str)
 Flotante → Entero   | int()         | int(5.9)                     | 5    (int)
 Flotante → Cadena   | str()         | str(3.14)                    | "3.14" (str)
 Cadena → Entero     | int()         | int("42")                    | 42   (int)
 Cadena → Flotante   | float()       | float("3.14")                | 3.14 (float)
 Booleano → Entero   | int()         | int(True)                    | 1    (int)
 Booleano → Flotante | float()       | float(False)                 | 0.0  (float)
 Entero → Booleano   | bool()        | bool(0)                      | False (bool)
 Flotante → Booleano | bool()        | bool(0.0)                    | False (bool)
 Cadena → Booleano   | bool()        | bool("")                     | False (bool)
 Lista → Tupla       | tuple()       | tuple([1, 2, 3])             | (1, 2, 3) (tuple)
 Tupla → Lista       | list()        | list((1, 2, 3))              | [1, 2, 3] (list)
 Conjunto → Lista    | list()        | list({1, 2, 3})              | [1, 2, 3] (list)
 Lista → Conjunto    | set()         | set([1, 2, 2, 3])            | {1, 2, 3} (set)
 Cadena → Lista      | list()        | list("hola")                 | ['h','o','l','a'] (list)
 Lista → Cadena      | ''.join()     | ''.join(['h','o','l','a'])   | "hola" (str)
 Entero → Binario    | bin()         | bin(10)                      | "0b1010" (str)
 Entero → Octal      | oct()         | oct(10)                      | "0o12"  (str)
 Entero → Hexadecimal| hex()         | hex(255)                     | "0xff"  (str)
 Binario → Entero    | int(x, 2)     | int("1010", 2)               | 10 (int)
 Octal → Entero      | int(x, 8)     | int("12", 8)                 | 10 (int)
 Hexadecimal → Entero| int(x, 16)    | int("ff", 16)                | 255 (int)

"""

# Este es un valor de tipo cadena donde no podemos realisar operaciones matematicas pero lo podemos convertir a entero
# para poder realisar operaciones matematicas 
numero_cadena = '10'
# 
numero_entero = int(numero_cadena)
print(numero_cadena+numero_cadena) # Esto te dara 1010
print(numero_entero+numero_entero) # Esto te dara la suma 10+10= 20

# con la funcion integrada type podemos ver que tipo de valor tiene el valor que pasamos como parametrosf
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)#Esto te dara ->    <class 'float'>
print(type(numero_flotante))


numero_entero = 25
numero_cadena = str(numero_entero)
print(numero_cadena+numero_cadena)# Esto te dara  ->  2525

# Convertir a booleano
# Tipo bool es Falso en los siguientes casos
# Si el valor es 0, cadena vacia, o None, entonces regresa False
# Regresa True, si el valor es distinto de 0, si es distinto de cadena vacia
# y tambien si es distinto de None 
numero_entero = 0
numero_bool = bool(numero_entero)


