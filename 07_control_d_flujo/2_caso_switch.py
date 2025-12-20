"""

match-case: Úsalo si tienes Python 3.10 o superior. Permite agrupar casos con | (OR) y usar lógica compleja.
Puedes consultar los detalles en la documentación oficial de Python.

"""


def actividad_del_dia(dia):
    match dia.lower():
        case "lunes":
            return "Inicio de semana: Reunión de planificación."
        case "martes" | "miércoles" | "jueves":
            return "Día de enfoque: Trabajo profundo."
        case "viernes":
            return "Cierre de semana: Reportes y limpieza de bandeja."
        case "sábado" | "domingo":
            return "Descanso: Fin de semana."
        case _:
            return "Error: Día no válido."

print(actividad_del_dia("Viernes")) # Resultado: Cierre de semana...



# Diccionarios: Ideales para velocidad y cuando solo necesitas devolver un valor fijo basado en una clave.

def actividad_del_dia_dicc(dia):
    semana = {
        "lunes": "Planificación",
        "martes": "Ejecución",
        "miércoles": "Ejecución",
        "jueves": "Revisión",
        "viernes": "Cierre"
    }
    # El método .get() permite definir un valor por defecto (el "default" del switch)
    return semana.get(dia.lower(), "Día no laboral o inválido")

print(actividad_del_dia_dicc("Lunes")) # Resultado: Planificación



# if-elif-else: Úsalo solo si las condiciones son muy pocas (2 o 3) o si trabajas en entornos muy antiguos.

def planificar_semana(dia, es_festivo):
    match dia.lower():
        case d if es_festivo:
            return f"Hoy es {d}, pero es festivo: ¡A descansar!"
        case "lunes":
            return "Reunión de equipo."
        case "viernes":
            return "Happy hour después del trabajo."
        case "sábado" | "domingo":
            return "Fin de semana."
        case _:
            return "Día de oficina estándar."

print(planificar_semana("Lunes", True)) # Resultado: Hoy es lunes, pero es festivo...
