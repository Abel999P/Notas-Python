"""
    -Decoradores
    
"""
print(f"decoradores".center(100, "-"))


def decorador(funcion):
    def funcion_decorada():
        print("Antes de la función")  # Código que se ejecuta antes
        funcion()                     # Llamada a la función original        
        print("Después de la función") # Código que se ejecuta después
    return funcion_decorada  # Devolvemos la nueva función decorada



@decorador  # Aplica el decorador a la función siguiente
def funcion_a_decorar():
    print("Hola desde la función a decorar")

# esto es igual a @decorador 

funcion_a_decorar()  # Ejecutamos la función decorada


print("funcion anidada".center(100,"-"))

def papas_fritas(papas):    
    def saladita ():
        print("hacer papas fritas")
        papas()
        print("con sal")
    return saladita

@papas_fritas
def hola():
    print("Este hola es de papas") 
    
#*@papas_frintas es lo mismo que hacer hola = papas_frintas(hola)

hola()



def sumar(num1,num2):
    return num1 + num2

def resta(num1,num2):
    return num1 - num2


def mul(z,x,random):
    return random(z,x) * random(z,x)

mul(5,4,resta)


def ejecutar_con_mensaje(func):
    def envoltura(*args, **kwargs):
        print(f"--- Ejecutando {func.__name__} ---")
        resultado = func(*args, **kwargs)
        print(f"--- {func.__name__} completado ---")
        return resultado
    return envoltura

@ejecutar_con_mensaje
def sumar(num1, num2):
    return num1 + num2

@ejecutar_con_mensaje
def resta(num1, num2):
    return num1 - num2

@ejecutar_con_mensaje
def mul(z, x, operacion):
    return operacion(z, x) * operacion(z, x)

# Se llama a la función mul que a su vez llama a resta
print(f"El resultado de mul con resta es: {mul(5, 4, resta)}")

# Se llama a la función sumar
print(f"El resultado de sumar es: {sumar(10, 5)}")
