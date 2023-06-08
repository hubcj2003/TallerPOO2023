#Potencia : **
#Raiz : sqrt

import math
arista = -1
while arista < 0:
    arista = int(input("Ingrese arista : "))
    if arista < 0:
        print("Ingresa de nuevo")
area = arista ** 2 * math.sqrt(3)
volumen = math.sqrt(2) *  arista ** 3 / 12
print("El area es : ", area)
#print(f"El area es : {area}")
#print("El area es : {}".format(area))
print("El volumen es : ", volumen)
