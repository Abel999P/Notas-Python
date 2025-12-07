


numeros = range(1,10+1)

# Sin usar comrension de listas 
numeros_pates = []
# Iteramos cada elemento de la lista 
for numero in numeros:
    if numero%2 == 0:
        numeros_pates.append(numero)

print(f"Numeros pares del 1 al 10: {numeros_pates}")

# Usando comprension de listas
# Sintaxis : nueva_lista = [expresion for elemento in iterables if condicion]

numeros_pares = [elemento for elemento in numeros if elemento%2==0 ]

print(f"Comprencion de lista {numeros_pares}")
