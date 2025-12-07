"""    
    -Funciones dentro de funciones(funciones anidadas)

"""

def funcion_externa():
    def funcion_interna():
        # Esta función solo existe dentro de funcion_externa
        print("Hola desde la función interna")
    funcion_interna()  # Llamamos a la función interna dentro de la externa

funcion_externa()  # Ejecutamos la función externa


#función anidadas. Su propósito es generar otras funciones.


# Toma un argumento 'moneda' que determinará el símbolo a usar más tarde.
def creador_de_formateador_dinero(moneda):
    
    # --------------------------------------------------
    # Zona de la función externa: Aquí preparamos el contexto.
    # --------------------------------------------------

    # Configuramos el símbolo de la moneda basado en el input.
    if moneda == "USD":
        simbolo = "$"
    elif moneda == "EUR":
        simbolo = "€"
    else:
        simbolo = moneda + " "
    
    # Definimos la función anidada/interna.
    # Esta función *no* se ejecuta aquí, solo se define.
    # Su propósito es realizar el formateo real del número.
    def formatear_dinero(cantidad):
        
        # --------------------------------------------------
        # Zona de la función anidada: El núcleo de la lógica.
        # --------------------------------------------------

        # ¡Punto clave! Accedemos a 'simbolo', que es una variable local 
        # de la función externa 'creador_de_formateador_dinero'.
        # La función anidada "captura" esta variable de su entorno superior.
        return f"{simbolo}{cantidad:,.2f}"
    
    # --------------------------------------------------
    # Fin de la función externa: Devolvemos la función interna.
    # --------------------------------------------------
    
    # Devolvemos la función 'formatear_dinero' en sí misma. 
    # No la estamos llamando (no ponemos paréntesis).
    # Estamos entregando la "receta" de la función, no el resultado de ejecutarla.
    return formatear_dinero

# ======================================================
# USO PRÁCTICO DEL CÓDIGO
# ======================================================

# 1. Creamos una función específica para USD.
# Al llamar a creador_de_formateador_dinero("USD"), 'simbolo' se fija como '$'.
# La función 'formatear_usd' resultante recuerda que su símbolo es '$'.
formatear_usd = creador_de_formateador_dinero("USD")

# 2. Creamos otra función específica para EUR.
# Al llamar a creador_de_formateador_dinero("EUR"), 'simbolo' se fija como '€'.
# La función 'formatear_eur' resultante recuerda que su símbolo es '€'.
formatear_eur = creador_de_formateador_dinero("EUR")

# 3. Usamos las funciones personalizadas:

monto_ejemplo = 1545.75
otro_monto = 99.99

# Llamamos a la función USD que creamos dinámicamente.
# Usa el símbolo '$' que fue encapsulado.
print(f"Monto en USD: {formatear_usd(monto_ejemplo)}")

# Llamamos a la función EUR que creamos dinámicamente.
# Usa el símbolo '€' que fue encapsulado.
print(f"Monto en EUR: {formatear_eur(otro_monto)}")

# La salida esperada es:
# Monto en USD: $1,545.75
# Monto en EUR: €99.99
