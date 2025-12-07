"""
    -Media de notas
def media(num_1,num_2,num_3):
    resultado = num_1 + num_2 + num_3
    resultado = resultado / 3
    return resultado 

# primer forma de usar la funcion media
notas = media(7,6,8)
print(notas)
# segunda forma de usar la funcion media
print(media(7,5,8))

"""
print("media notas".center(100,"-"))

def media_notas(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3)/3     
    
# primera forma de usar la funcion media
notas = media_notas(7, 6, 5)
print(notas)

# segunda forma de usar la funcion media
print(media_notas(7,3,8))
