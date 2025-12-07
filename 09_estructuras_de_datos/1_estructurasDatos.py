# ==========================================================
# 🧩 ESTRUCTURAS DE DATOS EN PYTHON
# ==========================================================

#
# - Cadenas
#



# -------------------------------
# 📋 LISTAS
# -------------------------------
"""
| Método / Operador               | Descripción                              | Ejemplo                           |
| ------------------------------- | ---------------------------------------- | --------------------------------- |
| `append(x)`                     | Agrega el elemento al final              | `[1,2].append(3) → [1,2,3]`       |
| `extend(iterable)`              | Une lista                                | `[1,2].extend([3,4]) → [1,2,3,4]` |
| `insert(i, x)`                  | Inserta `x` en posición `i`              | `[1,2].insert(1,9) → [1,9,2]`     |
| `remove(x)`                     | Elimina primera aparición de `x`         | `[1,2,2].remove(2) → [1,2]`       |
| `pop([i])`                      | Elimina y devuelve elemento en `i`       | `[1,2,3].pop() → 3`               |
| `clear()`                       | Vacía la lista                           | `[1,2].clear() → []`              |
| `index(x,[start],[end])`        | Índice de primera aparición              | `[1,2,2].index(2) → 1`            |
| `count(x)`                      | Cantidad de veces que aparece `x`        | `[1,2,2].count(2) → 2`            |
| `sort(key=None, reverse=False)` | Ordena la lista                          | `[3,1].sort() → [1,3]`            |
| `reverse()`                     | Invierte la lista                        | `[1,2,3].reverse() → [3,2,1]`     |
| `copy()`                        | Devuelve copia superficial               | `[1,2].copy() → [1,2]`            |

"""

print("\n=== LISTAS ===")

# Las listas pueden contener distintos tipos de datos
lista = [29, True, 3.1415, "El número de Avogadro sí que mola"]

print("Lista original:", lista)
print("Último elemento:", lista[-1])
print("Elementos del índice 1 al 2:", lista[1:3])

# Modificación de un elemento
lista[2] = "He cambiado este elemento"
print("Después de cambiar un elemento:", lista)

# Reemplazo con otra lista
lista[2] = [3, 2, 1]
print("Elemento reemplazado por una lista:", lista)

# Largo de la lista
print("Longitud de la lista:", len(lista))

# Ejemplo con métodos comunes
lista_nueva = [1, 2, 3, 4, 5]
lista_nueva.append(3)     # Agrega un elemento al final
print("Después de append:", lista_nueva)

print("Cantidad de veces que aparece el 3:", lista_nueva.count(3))
print("Índice del número 4:", lista_nueva.index(4))

lista_nueva.remove(3)     # Elimina la primera aparición de 3
print("Después de remove:", lista_nueva)


# -------------------------------
# 🧱 TUPLAS
# -------------------------------

"""
| Método                   | Descripción                       | Ejemplo                |
| ------------------------ | --------------------------------- | ---------------------- |
| `count(x)`               | Cantidad de veces que aparece `x` | `(2,2,2).count(2) → 3` |
| `index(x,[start],[end])` | Índice de primera aparición       | `(1,2,3).index(2) → 1` |
"""


print("\n=== TUPLAS ===")

# Las tuplas son inmutables (no se pueden modificar)
tupla = ("¿La tierra es plana?", True, False)
print("Tupla:", tupla)

# Acceso a elementos
print("Primer elemento:", tupla[0])
print("Segundo elemento:", tupla[1])
print("Tercer elemento:", tupla[2])

# Métodos disponibles
print("Veces que aparece True:", tupla.count(True))
print("Índice de False:", tupla.index(False))

# Diferencia entre (1) y (1,)
print("(1) es un número:", type((1)))
print("(1,) es una tupla:", type((1,)))


# -------------------------------
# 🔢 CONJUNTOS (SET)
# -------------------------------

"""
| Método / Operador                   | Descripción                              | Ejemplo                       |        |                  |
| ----------------------------------- | ---------------------------------------- | ----------------------------- | ------ | ---------------- |
| `add(x)`                            | Agrega elemento                          | `{1,2}.add(3) → {1,2,3}`      |        |                  |
| `remove(x)`                         | Elimina elemento (error si no existe)    | `{1,2}.remove(2) → {1}`       |        |                  |
| `discard(x)`                        | Elimina si existe                        | `{1,2}.discard(3) → {1,2}`    |        |                  |
| `pop()`                             | Elimina y devuelve un elemento aleatorio | `{1,2}.pop() → 1`             |        |                  |
| `clear()`                           | Vacía el set                             | `{1,2}.clear() → set()`       |        |                  |
| `copy()`                            | Devuelve copia                           | `{1,2}.copy() → {1,2}`        |        |                  |
| `union(*sets)` / `                  | `                                        | Unión                         | `{1,2} | {2,3} → {1,2,3}` |
| `intersection(*sets)` / `&`         | Intersección                             | `{1,2} & {2,3} → {2}`         |        |                  |
| `difference(*sets)` / `-`           | Diferencia                               | `{1,2} - {2,3} → {1}`         |        |                  |
| `symmetric_difference(other)` / `^` | Diferencia simétrica                     | `{1,2} ^ {2,3} → {1,3}`       |        |                  |
| `issubset(other)`                   | True si es subconjunto                   | `{1} <= {1,2} → True`         |        |                  |
| `issuperset(other)`                 | True si es superconjunto                 | `{1,2} >= {1} → True`         |        |                  |
| `isdisjoint(other)`                 | True si no tienen elementos en común     | `{1} .isdisjoint({2}) → True` |        |                  |

"""

print("\n=== CONJUNTOS ===")

# Un conjunto elimina duplicados automáticamente
print("Conjunto vacío:", set())

print("Conjunto a partir de lista:", set([5, 2, 5, 1, 1.5]))
print("Conjunto a partir de tupla:", set((5, 2, 5, 1, 1.5)))
print("Conjunto a partir de cadena:", set("52511.5"))

conjunto = {2, 3, 3, 4}
conjunto_2 = {5, 3, 5, 6}
conjunto_3 = {4, 2}

print("Conjunto 1:", conjunto)
print("Conjunto 2:", conjunto_2)
print("Conjunto 3:", conjunto_3)

# Operaciones comunes con conjuntos
conjunto.add(1)
print("Después de add(1):", conjunto)

conjunto.remove(1)
print("Después de remove(1):", conjunto)

print("Intersección con conjunto_2:", conjunto.intersection(conjunto_2))
print("¿conjunto_2 es subconjunto de conjunto?:", conjunto_2.issubset(conjunto))
print("¿conjunto_3 es subconjunto de conjunto?:", conjunto_3.issubset(conjunto))


# -------------------------------
# 📚 DICCIONARIOS
# -------------------------------
"""
| Método                     | Descripción                             | Ejemplo                                                 |
| -------------------------- | --------------------------------------- | ------------------------------------------------------- |
| `get(key, default=None)`   | Devuelve valor o default si no existe   | `{1:'a'}.get(2,'x') → 'x'`                              |
| `keys()`                   | Devuelve claves                         | `{1:'a',2:'b'}.keys() → dict_keys([1,2])`               |
| `values()`                 | Devuelve valores                        | `{1:'a',2:'b'}.values() → dict_values(['a','b'])`       |
| `items()`                  | Devuelve pares clave-valor              | `{1:'a',2:'b'}.items() → dict_items([(1,'a'),(2,'b')])` |
| `pop(key)`                 | Elimina y devuelve valor                | `{1:'a',2:'b'}.pop(1) → 'a'`                            |
| `popitem()`                | Elimina y devuelve último par           | `{1:'a'}.popitem() → (1,'a')`                           |
| `clear()`                  | Vacía diccionario                       | `{1:'a'}.clear() → {}`                                  |
| `update(other_dict)`       | Actualiza con otro diccionario          | `{1:'a'}.update({2:'b'}) → {1:'a',2:'b'}`               |
| `setdefault(key, default)` | Devuelve valor o crea clave con default | `{1:'a'}.setdefault(2,0) → 0`                           |
| `copy()`                   | Devuelve copia superficial              | `{1:'a'}.copy() → {1:'a'}`                              |

"""
print("\n=== DICCIONARIOS ===")

# Un diccionario almacena pares clave: valor
diccionario = {1: "Uno", 2: "Dos"}
diccionario[3] = "Tres"  # Agregar nuevo par
print("Diccionario:", diccionario)

# Creación a partir de lista de tuplas
dict_lista_tuplas = dict([(1, "Uno"), (2, "Dos"), (3, "Tres")])
print("Desde lista de tuplas:", dict_lista_tuplas)

# Creación con argumentos nombrados
dict_lista_string = dict(Uno=1, Dos=2, Tres=3)
print("Desde argumentos nombrados:", dict_lista_string)

# Diccionario con distintos tipos de claves
dict_tipos = {
    1: "integer",
    2.2: "float",
    "texto": "string",
    (1, 2): "tupla"
}
print("Diccionario con distintos tipos de clave:", dict_tipos)

# Si se repite una clave, se sobrescribe el valor
dict_repeticion = {1: "Primero", 1: "Último"}
print("Clave repetida (solo queda el último):", dict_repeticion)

# Métodos útiles
print("\nClaves:", diccionario.keys())
print("Valores:", diccionario.values())
print("Elementos (pares clave-valor):", diccionario.items())

# Acceso y modificación
valores = diccionario.values()
print("Valores antes del cambio:", list(valores))
diccionario[1] = "One"   # Modificamos el valor de la clave 1
print("Valores después del cambio:", list(valores))

# Eliminación de elementos
diccionario.pop(2)
print("Diccionario final:", diccionario)
