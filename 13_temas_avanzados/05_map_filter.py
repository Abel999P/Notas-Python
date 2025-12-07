
# El uso de map y lambda podemos usarlo en conjunto para mapear una operacion en cada elemento en el que estamos iterando 

# Con map y lambda 
# Creamos una lista de numeros 
numeros = [1,2,3,4,5,6]

# Aplicar una funcion lambda para obtener el cuadrado de cada numero 

cuadrados = list(map(lambda x : x ** 2,numeros))

print(cuadrados)


# con filter y lambda 
# filtrar elementos de un iterable 

pares = list(filter(lambda x : x%2 == 0,numeros))

print(pares)
