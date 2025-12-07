# esta variable edad no es una variable de instancia
#edad = 20

"""
Variable de instancia 
es cunado esta variable se relaciona con una instancia de una clase 

Variable de clase 
es cuando una variable esta relacionada directamento con la clase 


Metodos de instancia 


Metodo de clase


Metodos staticos 


Metodos especiales o magicos 


"""

class Persona():
 #Variable de clase es una variable que sera compartida por todas las instancias
    contador_personas = 0 
    
    def __init__(self,nombre,nacionalidad):
        self.nombre = nombre 
        self.nacionalidad = nacionalidad
        Persona.contador_personas += 1
        self.id_persona = Persona.contador_personas 

    def despedir(self):
        print("Te Saludo")

    @classmethod
    def correr(cls):
        print(f"Estoy corriendo ...")

    @staticmethod
    def nadar():
        print("Estoy nadando")

    def __str__(self) -> str:
        return f"""Persona : {self.id_persona}
Nombre : {self.nombre}
Nacionalidad : {self.nacionalidad}
Dir. mem. = {object.__str__(self)}
"""
    

persona1 = Persona("Martin","Argentina")
perosna2 = Persona("Lucas","MEX")
persona3 = Persona("Ana","USA")
print(persona1.nombre)
print(persona1.id_persona)
print(perosna2.nacionalidad)
print(Persona.contador_personas)
print(persona3)
print()



"""


"""

import math

class Libro:
    """
    Clase que representa un libro, mostrando varios métodos mágicos comunes (dunder methods).
    """
    def __init__(self, titulo, autor, paginas):
        """
        __init__: El constructor. Se llama al crear una nueva instancia.
        Inicializa los atributos básicos del objeto.
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        print(f"DEBUG: Se ha inicializado el libro '{self.titulo}'.")

    def __del__(self):
        """
        __del__: El destructor. Se llama cuando el objeto es destruido
        o eliminado de la memoria (con 'del' o por el garbage collector).
        """
        print(f"DEBUG: El libro '{self.titulo}' ha sido eliminado de la memoria.")

    def __str__(self):
        """
        __str__: Representación legible para humanos.
        Se invoca con print(objeto) o str(objeto).
        Debe devolver una cadena amigable.
        """
        return f"'{self.titulo}' por {self.autor}"

    def __repr__(self):
        """
        __repr__: Representación "oficial" o canónica para desarrolladores.
        Se invoca en la consola interactiva o con repr(objeto).
        Debería permitir recrear el objeto si es posible.
        """
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', paginas={self.paginas})"

    def __len__(self):
        """
        __len__: Define el comportamiento de la función len().
        Permite medir la "longitud" del objeto (en este caso, las páginas).
        """
        return self.paginas

    # --- Métodos Mágicos para Comparación (Sobrecarga de Operadores) ---

    def __eq__(self, other):
        """
        __eq__: Define el comportamiento del operador de igualdad (==).
        Dos libros son "iguales" si tienen el mismo título y autor.
        """
        if isinstance(other, Libro):
            return self.titulo == other.titulo and self.autor == other.autor
        return NotImplemented

    def __gt__(self, other):
        """
        __gt__: Define el comportamiento del operador "mayor que" (>).
        Un libro es "mayor" que otro si tiene más páginas.
        """
        if isinstance(other, Libro):
            return self.paginas > other.paginas
        return NotImplemented

    # También existen __ne__ (!=), __lt__ (<), __le__ (<=), y __ge__ (>=)


# --- Demostración del Uso ---

print("--- 1. Inicialización y Representación ---")
# __init__ es llamado automáticamente aquí:
libro1 = Libro("Cien años de soledad", "Gabo", 471)
libro2 = Libro("Don Quijote", "Cervantes", 1024)

# __str__ es llamado aquí:
print(f"Mi libro favorito es: {libro1}")

# __repr__ es llamado aquí (útil para depuración):
print(f"Representación de depuración: {repr(libro2)}")

print("\n--- 2. Uso de len() ---")
# __len__ es llamado aquí:
print(f"'{libro1.titulo}' tiene {len(libro1)} páginas.")

print("\n--- 3. Comparación de Objetos ---")
# __eq__ es llamado aquí:
print(f"¿Son libro1 y libro2 el mismo libro? {libro1 == libro2}") # False

# __gt__ es llamado aquí:
print(f"¿Es libro2 más largo que libro1? {libro2 > libro1}") # True

print("\n--- 4. Demostración del Destructor ---")
# __del__ se llama cuando eliminamos explícitamente el objeto:
del libro1
# __del__ para libro2 se llamará automáticamente cuando termine el programa
# o cuando ya no haya referencias a él.

