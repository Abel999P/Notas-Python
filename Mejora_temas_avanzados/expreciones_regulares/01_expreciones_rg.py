"""

Articulo de expreciones regulares :
https://relopezbriega.github.io/blog/2015/07/19/expresiones-regulares-con-python/

"""

import re 


print(re.search(r"z","Taza"))

print(re.search("\d\d\d","Ta122za"))

mi_patron = re.compile("\d\d\d")
print(mi_patron.search("Ta122za").group())


if (re.search("\Aa[0-9].*(end|fin)$","a4 es una marca de fin")):
    print("Se encontro el patron...")


print(re.sub(r"\d","-","hola@g2mail120.com",2))



reg = re.compile(r"ac",re.IGNORECASE)
print(reg.search("pedro cualquierAC"))



