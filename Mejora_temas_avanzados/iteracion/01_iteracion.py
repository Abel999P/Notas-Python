

lenguajes = ["Java","JavaScript","PHP","C","Ruby","Python"]
print(["JavaScript" in lenguajes])


for i in open("doc.txt"):
    print(i)


"""
    Generadores

"""

def generaPares(limite):
    num = 1
    while num<limite:
        yield num * 2
        num+=1 
    


if __name__=="__main__":
    devuelve_pares = generaPares(10)

    print(next(devuelve_pares))
    print(next(devuelve_pares))
    print(next(devuelve_pares))
    print(next(devuelve_pares))
    print(next(devuelve_pares))
    print(next(devuelve_pares))
    print(next(devuelve_pares))
    print(next(devuelve_pares))
    print(next(devuelve_pares))
