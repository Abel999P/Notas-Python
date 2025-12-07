#import mi_modulo #* aqui importamos TODO lo que está dentro del archivo mi_modulo.py

#print(mi_modulo.variable) #* aquí imprimimos lo q está dentro de la variable "variable" del archivo mi_modulo.py

#print(mi_modulo.funcion()) #*aqui imprimimos la funcion dentro del archivo mi_modulo.py

#Lucas = mi_modulo.MI_clase("Lucas") # Mas adelante veremos clases 
#Lucas.saludar()


""" 
Podemos usar la sentencia "as" para renombrar el módulo y facilitarnos la llamada a su contenido
"""

#import mi_modulo as mo 

#print(mo.variable)
#print(mo.funcion())


"""
En vez de importar el módulo entero como un objeto, podemos importar el contenido de
este a través de la sentencia from. Desde mi_modulo, importamos la variable. Probamos
a imprimir la variable y ejecutar la función. Como ves, solo se imprime la variable porque
la función no se ha importado.
"""

#from mi_modulo import variable 
#print(variable)

"""
Podemos importar lo que queramos, separado
por comas. Incluso renombrar lo que importemos.
"""
#from mi_modulo import variable as va , funcion as fu
#print(va)
#print(fu)


"""
También podemos importar, todo el contenido
del módulo directamente, para ello, escribimos from, el módulo, import y, asterisco. Como
ves, podemos usar todo. Ten cuidado, Python importará toooodo el
contenido, así que si solo vas a usar unas pocas cosas del módulo, es una buena práctica
solo que importes lo que vayas a usar, concretamente con módulos muy grandes.
"""
# from mi_modulo import * es igual a import mi_modulo
#from mi_modulo import *


"""
El namespace o espacio de nombres es el conjunto de todos los nombres definidos, es decir,
las variables, funciones, clases, etc. Se puede visualizar en una lista, con la función
(Namespace y hack)
integrada en dir(). En esta lista, podemos ver nombres que proporciona
Python por defecto como __file__ donde se encuentra la ruta del fichero, __name__ que
define el nombre del fichero, o el propio módulo que hemos importado.
"""
#print("el dir".center(100,"-"))
#import mi_modulo as mo
#print(dir())

"""
¡Atento! Te voy a contar un hack de mucha utilidad con __name__. Si lo imprimes en tu
programa principal, no coincide con el nombre del archivo. Python sustituye el
nombre por el string __main__ si se está ejecutando como programa principal. 
Por si no lo sabes, main significa principal. Para que veas que no te estoy engañando vamos
a ver también el __name__ del módulo.
Efectivamente, tiene el nombre que le hemos puesto.
"""
#import mi_modulo as mo
#print(__name__)
#print(mo.__name__)

"""
sobre rutas: Cuando importo un módulo se crea esta carpeta(__pycache__)
¿Qué mierdas es esto? No te rayes, es una carpeta donde Python guarda
los módulos ya compilados para acelerar la ejecución.
"""
#import mi_modulo


"""
Vale, vale ¿Y si mi módulo no está en la raíz del archivo que estoy ejecutando, sino
en un subdirectorio? Fácil, escribimos la ruta en el import separado
por puntos.
"""

from carpeta.mo_carpeta import variable as va ,funcion as fu ,MI_clase as mc



"""
Bien pero, ¿y si no está dentro de esta
carpeta? ª? Para eso tengo que explicarte cómo Python busca módulos en dos pasos:
Primero, busca si el nombre coincide con alguno de esta tupla, si coincide, carga el módulo
integrado correspondiente. Estos módulos integrados están escritos
en C y Python ya los incorpora por cuestiones de velocidad.
"""

#import sys
#print(sys.builtin_module_names)


"""
Segundo, comprueba en las rutas dentro de esta lista.
Donde la primera es la raíz del fichero que está ejecutando, y el resto, son rutas de
los módulos que instalastes con Python. Por eso, si tu módulo no está aquí, puedes
añadirlo a una de estás rutas o añadir tu propia ruta a la lista.
¿Y si llamo a mi módulo igual que las instaladas? ¿Cuál importa?
Seguirá el orden que te acabo de decir, por lo que si llamas a tu módulo “math” que
coincide con uno de los módulos de C, ignorará el tuyo peeeeeeeeeeero si lo llamas random,
un módulo de Python, dará preferencia al tuyo.
"""

#import sys
#print(sys.path)
#sys.path.append("Tu ruta para agregar tu modulo")
##Comprueba si se añadio a la lista 
#print(sys.path)
