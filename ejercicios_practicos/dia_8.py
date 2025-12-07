#contact = {
#    "name": "John Doe",
#    "phone": "123-456-7890",
#    "email": "john@example.com"
#}
#
#for key,value in contact.items():
#    print(f"{key}: {value}")
#
#if "email" in contact:
#    print("Correo electrónico encontrado.")
#else:
#    print("Correo electrónico no encontrado.")
#


contactos = {}

def mostrar_menu():
    print("\n--- Menú de la libreta de contactos ---")
    print("1. Añadir contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")

def añadir_contacto():
    global contactos
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el número de teléfono: ")
    email = input("Introduce el correo electrónico: ")
    contactos[nombre] = {"telefono": telefono, "email": email}
    print(f"Contacto {nombre} añadido correctamente.")



def ver_contactos():
    if contactos:
        print("\n--- Lista de contactos ---")
        for nombre, detalles in contactos.items(): # el metodo .items() devolvera la llave y el valor por separados y se guardaran en las variables nombre y detalle
            print(f"Nombre: {nombre}")
            print(f"  Teléfono: {detalles['telefono']}")
            print(f"  Email: {detalles['email']}")
    else:
        print("No hay contactos en la libreta.")

def buscar_contacto():
    nombre = input("Introduce el nombre del contacto a buscar: ")
    if nombre in contactos:
        detalles = contactos[nombre]
        print(f"Contacto encontrado: {nombre}")
        print(f"  Teléfono: {detalles['telefono']}")
        print(f"  Email: {detalles['email']}")
    else:
        print("Contacto no encontrado.")

def editar_contacto(): #definimos funcion "editar_contacto"
    nombre = input("Introduce el nombre del contacto a editar: ") #aqui pedimos q escriban el nombre y se guarda en la variable nombre
    if nombre in contactos: # aqui se buscará el contacto y se agregarán los nuevos datos q el usuario debe introducir         
        telefono = input("Introduce el nuevo número de teléfono: ") 
        email = input("Introduce el nuevo correo electrónico: ")
        contactos[nombre] = {"telefono": telefono, "email": email} # Buscamos en el dic contactos con el nombre ingresado y remplazamos el valor con las varables telefono y email
        print(f"Contacto {nombre} actualizado correctamente.")
    else:
        print("Contacto no encontrado.")


def eliminar_contacto():
    nombre = input("Introduce el nombre del contacto a eliminar: ")
    if nombre in contactos:# si nombre se encuentra dentro de contactos
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado correctamente.")
    else:
        print(f"El contacto {nombre} no se encontró en la libreta de contactos.")



while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-6): ")
    if opcion == "1":
        añadir_contacto()
    elif opcion == "2":
        ver_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        editar_contacto()
    elif opcion == "5":
        eliminar_contacto()
    elif opcion == "6":
        print("Saliendo de la libreta de contactos. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

    
    
