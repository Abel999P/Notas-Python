
"""ejemplo de los usos con un generador de email """


nombre = "  Ubaldo Acosta Soto "
empresa= "Global Mentoring"
dominio = ".com.mx"

norm_nombre = nombre.strip()
norm_nombre = nombre.replace(" ",".")
norm_nombre = norm_nombre.lower()

print(norm_nombre)
norm_empreza = empresa.replace(" ","").lower()

print(norm_empreza)

dominio_completo = f"@{norm_empreza}{dominio}"
email = norm_nombre+dominio_completo

print(f"\n{email}")
