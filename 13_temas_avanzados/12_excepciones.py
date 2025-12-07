
"""
    Manejo de Excepciones 

"""

def dividir(numerador,denominador):

    try:
        resultado =  numerador /  denominador 
        print(f"Resultado de la division : {resultado}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Finalizando el programa...\n")
    
dividir(10,2)
dividir(10,"4")
dividir(10,0)
