"""
    -Funciones lambda

# Una función lambda es una función anónima (sin nombre) que se escribe en una sola línea.

"""
print("funcion lambda".center(100,"-"))

suma = lambda x, y: x + y
print(suma(3, 5))  # Llama a la función y muestra 8
print(suma(2,5))



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar solo los números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)
# Resultado: [2, 4, 6, 8, 10]

# --- Explicación del funcionamiento ---
# filter() itera sobre cada número en 'numeros'.
# Por cada número (x), llama a la función lambda.
# La lambda 'lambda x: x % 2 == 0' comprueba si el número es par.
# Si la lambda devuelve True (por ejemplo, para x=2), el número se incluye en el resultado.
# Si devuelve False (por ejemplo, para x=1), el número se omite.
# Usamos list() para convertir el iterador resultante en una lista visible.
