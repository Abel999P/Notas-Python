
def dividir(numerador,denominador): 
    try:
        if 0 == numerador:
            raise Exception("El numerador no puede ser cero")
        elif denominador == 0 :
            raise Exception("El denominador no puede ser cero")

        resultado = numerador / denominador 
        print(f"La resultado de la divicion es : {resultado}")
    except Exception as e:
        print(f"Error : {e}")
    else:
        print("No se lanso ninguna excepcion")
    finally:
        print("Fin de la funcion ...\n")

dividir(10,0)
dividir(10,"10")

