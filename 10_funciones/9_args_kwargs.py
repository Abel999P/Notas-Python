"""
    -Argumentos *args y **kwargs

def funcion(*args, **kwargs):
    # *args recopila los argumentos posicionales en una tupla
    # **kwargs recopila los argumentos nombrados en un diccionario
    print("Argumentos posicionales:", args)
    print("Argumentos nombrados:", kwargs) 

# Llamamos a la función pasando argumentos normales y con nombre
funcion(1, 2, 3, nombre="Juan", edad=30)


"""

print("Argumentos *args y **kwargs".center(100,"-"))


def funcion2(*args, **kwargs):
    # *args recopila los argumentos posicionales en una tupla
    # **kwargs recopila los argumentos nombrados en un diccionario
    print("Argumentos posicionales:", args)
    print("Argumentos nombrados:", kwargs) 
    
# Llamamos a la función pasando argumentos normales y con nombre
funcion2(1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16, nombre="Juan", edad=30, departamento="2 ambientes")


# Definimos una función llamada 'funcion' que acepta dos tipos de parámetros variables:
# 1. '*args': Recibe un número variable de argumentos posicionales y los empaqueta en una tupla llamada 'args'.
# 2. '**kwargs': Recibe un número variable de argumentos de palabra clave (con nombre) y los empaqueta en un diccionario llamado 'kwargs'.
def funcion(*args, **kwargs):
    # La función simplemente devuelve las dos colecciones que ha creado:
    # Primero la tupla 'args', y segundo el diccionario 'kwargs'.
    return args, kwargs

# Llamamos a la función 'funcion' con varios datos:
# Argumentos posicionales: 1, 2, 3, 4, 5, 6, 7 (estos irán a parar a 'args')
# Argumentos de palabra clave: nombre="Juan", edad=30, departamento="2 ambientes" (estos irán a parar a 'kwargs')
# El resultado de la función (una tupla y un diccionario) se desempaqueta en dos variables locales:
# 'tupla' recibirá la tupla de args.
# 'diccionario' recibirá el diccionario de kwargs.
tupla, diccionario = funcion(1,2,3,4,5,6,7,nombre="Juan",edad=30,departamento="2 ambientes")

# Imprimimos el tipo de la variable 'tupla'.
# Esperamos que sea <class 'tuple'> porque *args crea una tupla.
print(f"{type(tupla)}") # -> espero que esto de una tupla pero no se XD

# Imprimimos el tipo de la variable 'diccionario'.
# Esperamos que sea <class 'dict'> porque **kwargs crea un diccionario.
print(f"{type(diccionario)}") # -> esto si se que dara un dic de diccionario



#*Ejemplo practico de *args y **kwargs

def registrar_operaciones(usuario, *acciones, **detalles):
    """
    Registra las operaciones realizadas por un usuario.
    
    Parámetros:
    - usuario (str): nombre del usuario.
    - *acciones: lista variable de acciones realizadas (por ejemplo, 'login', 'descarga', 'borrado').
    - **detalles: información adicional sobre las acciones (por ejemplo, fecha='2025-11-07', ip='192.168.1.10').
    
    """

    print(f"Usuario: {usuario}")
    
    # Si el usuario realizó acciones, las mostramos
    if acciones: # si acciones tiene algo dentro if tomara que es True pero si no es False 
        print("Acciones realizadas:") #
        for enumeracion, accion in enumerate(acciones, start=1): # enumerate() devolvera el indice 
            print(f"  {enumeracion}. {accion}")
    else:
        print("No se registraron acciones.")
    
    # Si se pasaron detalles adicionales (kwargs)
    if detalles:
        print("\nDetalles adicionales:")
        for clave, valor in detalles.items():
            print(f"  {clave}: {valor}")
    else:
        print("\nNo se proporcionaron detalles adicionales.")
    
    print("-" * 40)


# Ejemplo de uso 1: con varias acciones y detalles
registrar_operaciones(
    "joel",
    "login", "cargar archivo", "cerrar sesión",
    fecha="2025-11-07",
    ip="192.168.1.23",
    exito=True
)


# Ejemplo de uso 2: sin acciones, pero con detalles
registrar_operaciones(
    "maria",
    fecha="2025-11-06",
    ip="10.0.0.8"
)


# Ejemplo de uso 3: solo acciones, sin kwargs
registrar_operaciones(
    "carlos",
    "login", "ver estadísticas"
)

