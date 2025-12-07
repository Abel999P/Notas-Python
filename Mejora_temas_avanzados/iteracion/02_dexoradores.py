

"""
    Decoradores
    
"""

def decorador(funcionComun):
    def envolver(*args,**kwargs):
        print("Funcion dexoradora Antes de la funcion")
        funcionComun()
        print(f"Funcion decorador Finalizando ...")
    return envolver 


@decorador 
def funcionComun():
    print(f"Funcion comun")


funcionComun()

