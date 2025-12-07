

nombre = input("Ingresa el nombre : ") #*se le dice al usuario que introduca el su nombre 
apellido = input("Ingresa el apellido : ") #*se le dice al usuario que introduca el su apellido 
nom_empresa = input("Ingresa el nombre de la empresa : ") #*se le dice al usuario que introduca el su nombre de su empresa


nombre = nombre.strip().lower().replace(" ",".") #*elimina los espacios del inicio y del final, pone las letras en minuscula,remplazar los espacios por puntos  
apellido = apellido.strip().lower().replace(" ",".") 
nom_empresa = nom_empresa.strip().lower().replace(" ","") + ".com.mx" #*elimina los espacios del inicio y del final, pone las letras en minuscula,remplazar los espacios por puntos y se le concatena (junta) .com.mex

print(f"{nombre +'.'+ apellido +'@'+ nom_empresa}") #*se imprimen y que concatenan las variable nombre, apellido, noombre de la empresa y se le agrega a la concateacion un @

