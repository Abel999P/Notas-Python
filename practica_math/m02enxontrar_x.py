import random
import math
# Aprender expreciones regulares para mejorar esto 
def manejar_fra(fra):
    if "/" in fra:
        palabra = fra.split("/")
        a = int(palabra[0])
        b = int(palabra[1])
        resultado = a/b
        return resultado
    else:
        resultado = float(fra)
        return resultado

def proporciones_n():
    import random
    n1 = random.randint(1, 10)
    d1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    d2 = random.randint(1, 10)

    lista_num = [n1, n2, d1, d2]
    lista_num[random.randint(0, 3)] = "x"
    print(lista_num)

    print(lista_num[0], "\t\t", lista_num[1])
    print("-- \t = \t --")
    print(lista_num[2], "\t\t", lista_num[3])
    print(" ")
    x = input("x = ")

    if lista_num[0] == "x":
        resultado = (lista_num[1]*lista_num[2])/lista_num[3]
    elif lista_num[1] == "x":
        resultado = (lista_num[0]*lista_num[3])/lista_num[2]
    elif lista_num[2] == "x":
        resultado = (lista_num[0]*lista_num[3])/lista_num[1]
    elif lista_num[3] == "x":
        resultado = (lista_num[0]*lista_num[2])/lista_num[1]

    if str(resultado) == x:
        print("Correcto !")
    else:   
        print("Incorrecto ! El resultado correcto es: ", resultado)

def decimal_a_fraccion_test():
    # usa cadena_a_frac()
    print("Convierte el siguiente decimal a una fracción")
    print("Usa / para escribir tu fracción")
    num = random.randint(1,4)
    decimal = round(random.random(), num)
    print(decimal)
    d = 10**num
    n = decimal*d
    ans_in = input("Fracción: ")
    if manejar_fra(ans_in)==decimal:
        print("¡Correcto! \n")
    else:
        print("Intenta de nuevo")
        print("La respuesta es ", n, "/", d)

# Fracción a porcentaje
def fraccion_a_porcentaje_test():
    import random
    print("Convierte la siguiente fracción a porcentaje")
    n = round(random.randint(1,99))
    d = round(random.randint(2,200))
    print(n, "/", d)
    percent = round(n/d*100,2)
    print("Redondea tu respuesta a dos decimales")
    ans = float(input("Porcentaje: "))
    if ans==percent:
        print("¡Correcto!")
    else:
        print("Intenta de nuevo")
        print("La respuesta es ", percent)


if __name__ == "__main__":
    fraccion_a_porcentaje_test()