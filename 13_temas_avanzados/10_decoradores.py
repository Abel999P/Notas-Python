


def decorador(funcion):
    def wrapper(*args,**kwargs):
        print("Antes de llamar a nustra funcion de saludar")
        resultado = funcion(*args,**kwargs)
        print("Despues de llamar a nuestra funcion de saludar")
        return resultado 
    return wrapper 

        

@decorador 
def saludar(nombre,apellido):
    print(f"Hola {nombre} y mi apellido es {apellido}")


saludar("Carlos","Dalto")


