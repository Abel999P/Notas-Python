# sintaxis : sorted(iterable,key=None,reverse=False)

empleados = ["Juan", "Pedro", "Maria"]

# Ordenar la lista
empleados_ordenados = sorted(empleados, reverse=True)
print(empleados_ordenados)

# Lista de diccionarios (CORRECCIÓN: usar lista en lugar de set)
empleados_dict = [
    {"Nombre": "Juan", "Salario": 3000},
    {"Nombre": "Maria", "Salario": 2500},
    {"Nombre": "Pedro", "Salario": 3500}
]

print("Original:", empleados_dict)

# Ordenar por salario (ascendente)
orden_por_salario = sorted(empleados_dict, key=lambda e: e["Salario"])
print("Por salario (asc):", orden_por_salario)

# Ordenar por salario (descendente)
orden_por_salario_desc = sorted(empleados_dict, key=lambda e: e["Salario"], reverse=True)
print("Por salario (desc):", orden_por_salario_desc)

# Ordenar por nombre
orden_por_nombre = sorted(empleados_dict, key=lambda e: e["Nombre"])
print("Por nombre:", orden_por_nombre)