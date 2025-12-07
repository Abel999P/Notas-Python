from random import randint 

numero = randint(1,10)

print(numero)

print("Sistema Generador de ID unico".center(100,"*")) #* centrar el titulo del proyecto 

nombre = input("Cual es tu nombre ") #* el usuario introduce su nombre
apellido = input("Cual es tu apellido ") #* el usuario introduce su apellido
anio_nacimiento = input("Cual es tu año de nacimiento (YYYY) ") #* el usuario introduce su año de nacimiento

# randint (1,s) si por que len() -> se transforma en un numero 

#Normalizar los valores 

#* elimina los espacios del principio y el final de la cadena, hacer que todo el texto esté en mayusculas, 
#* da un numero aleatorio dependiendo de los caracteres que esten dentro del nombre/apellido
nombre = nombre.strip().upper()[0:randint(0,len(nombre))] #!esto es igual q en matematicas, de adentro hacia afuera
apellido = apellido.strip().upper()[0:randint(0,len(apellido))] 

#* elimina los espacios del principio y el final de la cadena, da un numero aleatorio 
#* dependiendo de los caracteres que esten dentro del año de nacimiento
anio_nacimiento = anio_nacimiento.strip()[2:randint(0,len(anio_nacimiento))] 

#* imprime los resultados
print(nombre)
print(apellido)
print(anio_nacimiento)


print("ID".center(100,"-")) #* centra el "ID" y agrega - a los lados.

print(f"{nombre+apellido+anio_nacimiento}") #* suma las variables para crear el ID".

"para mi si estan bien los comentarios"