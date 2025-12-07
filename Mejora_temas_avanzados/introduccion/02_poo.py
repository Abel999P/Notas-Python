
"""
    Polimorfismo
La posivilidad de que un metodo se comporte diferente con distintos objetos

"""


class Perro():
    def avanzar(self):
        print("Tengo 4 patas")

class Perico():
    def avanzar(self):
        print("Volar")


def mover(animal):
    animal.avanzar()

perro1 = Perro()
perico1 = Perico()


#mover(perico1)



"""
    Introspección 

"""

class Intro():
    pepe = "Hola"

    def __init__(self,valor) -> None:
        self.valor = valor

    def segundo(self):
        print("Segundo")

    def tercero(self):
        print("Tercero")


dato1 = Intro("Valor")

#print(dir(dato1))

#datos_d = dir(dato1)
#for i in datos_d:
#    print(i)

# Pregunta si es una instancia de una clase pasando el objeto y luego la clase 
#print(isinstance(dato1,Intro))


# Pregunta si tenemos una variable de clase donde se distinge entre mayusculas  
#print(hasattr(dato1,"pepe"))

"""
    Abstracción 
la simplificación de un concepto

"""

class Lavadora():

    def __init__(self) -> None:
        pass

    def lavar(self,temp="caliente"):
        self._llenar_tanque_de_agua(temp)
        self._aniadir_jabon()
        self._lavar()
        self._centrifugar()


    def _llenar_tanque_de_agua(self,temp):
        print(f"Llenando el tanque con agua {temp}")

    def _aniadir_jabon(self):
        print("Añadiendo jabon")

    def _lavar(self):
        print("Lavando")

    def _centrifugar(self):
        print("Centrifugando la ropa")

"""
    Herencia

"""

class Personal():

    def __init__(self,antiguedad,especialidad):
        self.especialidad = especialidad
        self.antiguedad = antiguedad 

    def Sueldo(self):
        if (self.especialidad == 'BF'):
            return 10 * self.antiguedad 
        else:
            return 15 * self.antiguedad 


class Supervisor(Personal):

    def __init__(self,cargo):
        super().__init__(5,cargo)

class Operador(Personal):
    def __init__(self,cargo):
        super().__init__(2,cargo)
    


if __name__=="__main__":
#    lavadora1 = Lavadora()
#    lavadora1.lavar()
    personal1 = Personal(10,"Jefe de Desarrollo")
    print(f"Sueldo del personal: {personal1.Sueldo()}")

    supervisor1 = Supervisor("BF")
    print(f"Sueldo del supervisor : {supervisor1.Sueldo()}")

    operador1 = Operador("Programador")
    print(f"Sueldo del operador : {operador1.Sueldo()}")    

