


def hallarSumatoria(n, b):
    suma = 0.0
    denominador = 4
    for i in range(1, n + 1): # 1 --- n - 1 
        suma = suma + pow(-1, i + 1) * i * 2 * b / denominador 
        denominador = denominador + 3
    #print("La suma es {:.3f}".format(suma))
    print("La suma es ",round(suma,3))

n = b = -1
while not(n > 0): # n < 0 or n > 120
    n = int(input("Ingrese n : "))
while not(b >=1 and b <= 5): # n < 0 or n > 120
    b = float(input("Ingrese b : "))
hallarSumatoria(n, b)