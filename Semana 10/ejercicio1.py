

#POTENCIA   pow()     **


def factorial(n):
    fac = 1
    for i in range(1, n + 1):# 5*4*3*2*1
        fac = fac * i
    return fac

def hallarSumatoria(n):
    suma = 0.0
    for i in range(1, n + 1): # 1 --- n - 1 
        suma = suma + i**2/ (2 *factorial(i))  #math.factorial(i)
    return suma

n = -1
while not(n > 0 and n <= 120): # n < 0 or n > 120
    n = int(input("Ingrese n : "))
print("La suma es ", hallarSumatoria(n))




#import math

#def factorial(n):
#    fac = 1
#    for i in range(1, n + 1):# 5*4*3*2*1
#        fac = fac * i
#    return fac

#def hallarSumatoria(n):
#    suma = 0.0
#    for i in range(1, n + 1): # 1 --- n - 1 
#        suma = suma + i**2/ (2 *math.factorial(i)) 
#    return suma

#n = -1
#while not(n > 0 and n <= 120): # n < 0 or n > 120
#    n = int(input("Ingrese n : "))
#print("La suma es ", hallarSumatoria(n))
