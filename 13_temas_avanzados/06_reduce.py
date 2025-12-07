
# la funcion reduce se encuentra en el modulo functools se utilisa para 
# aplicar una funcion epsecifica de dos argumentos de manera secuencual a
# los elementos de un iterable reduciendolos a un solo valor acumulado.


from functools import reduce 


# reduce y map 
numeros = [1,2,3,4,5,6]

suma_acumulativa = reduce(lambda x,y: x+y,numeros)
print(suma_acumulativa)
