import random
def generar(lista, n):
    for i in range(n):
        lista.append(random.randint(1, 9))
def mostrar(lista):
    for i in lista:#[5][8][9]
        print(f"[{i}]", end="")
    print()
def repeticiones(lista):
    for i in range(1, 10):
        print(f"Cantidad de {i} = ", lista.count(i))
def remplazar(lista):
    primos = [2,7,5, 3]
    #print("El indice es : ", primos.index(5))
    #primos = lista.copy()
    #primos.insert(1, 3)
    #primos.pop(0)
    #primos.reverse()
    #primos.sort()
    #primos.remove(5)
    #print("El indice es : ", primos)
    #for i in range(len(lista)):
    #    if lista[i] in primos:
    #        lista[i]+=1

n = -1
lista = list()
while not(n >= 1 and n <= 40): 
    n = int(input("Ingrese n : "))
generar(lista, n)
mostrar(lista)
repeticiones(lista)
remplazar(lista)
mostrar(lista)