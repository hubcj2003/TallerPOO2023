#EJERCICIO 1

def menu():
    op = -1
    while not(op >=1 and op <= 3):
        print("Menú de opciones    ")
        print("1. Calcular la serie")
        print("2. Gráfico          ")
        print("3. Fin              ")
        op = int(input("Ingrese la opcion: "))
    return op
def calcularSerie(n, a):
    suma = 0
    for i in range(1, n + 1):
        suma+= pow(-1, i + 1)*(2*i -1) * pow(a, pow(2, i -1)) / (2 * i)
    print("El valor de la suma es : ", suma)
def graficar(n):
    for i in range(1, n +1):
        cont = 1
        for esp in range(n - i):
            print(end= "  ")
        for j in range(1, i * 2):
            print(cont, end=" ")
            if j < i:
                cont +=1
            else:
                cont-= 1
        print()

op = -1
while op != 3: 
    op = menu()
    if op == 1:
        n =-1
        while not(n > 0 and n < 21):
            n = int(input("Ingresar n : "))
        a =-1
        while not(a > 0.5 and a <= 2):
            a = float(input("Ingresar a : "))
        calcularSerie(n, a)
    elif op == 2: 
        n =-1
        while not(n >=1 and n <= 9):
            n = int(input("Ingresar n : "))
        graficar(n)

#EJERCICIO 2

import random as r

def generar(n):
    caracteres = []
    for i in range(n):
        caracteres.append(chr(r.randint(65, 90)))
    return caracteres
def esVocal(letra):
    return letra in "AEIOU"
def vocalesAlternar(caracteres):
    for i in range(len(caracteres) - 6):
        if(esVocal(caracteres[i]) and esVocal(caracteres[i + 2])  and esVocal(caracteres[i + 4]) 
           and esVocal(caracteres[i + 6]) and caracteres[i + 6] > caracteres[i + 4]
           and caracteres[i + 4] > caracteres[i + 2]and caracteres[i + 2] > caracteres[i]):
            print("Se encontraron vocales en orden ascendente y se ubica en ", i)
def ordnearPosicionesImpares(caracteres):
    #print(caracteres[1::2])
    #print(sorted(caracteres[1::2], reverse=True))
    caracteres[1::2] = sorted(caracteres[1::2], reverse=True)
    print(caracteres)
n =-1
while not(n > 0 and n < 50):
    n = int(input("Ingresar n : "))
caracteres = generar(n)
print(caracteres)
vocalesAlternar(caracteres)
ordnearPosicionesImpares(caracteres)

#EJERCICIO 3

import random as r

class Encunta:
    __edad = 18
    __sexo = 'F'
    __prueba = 'R'
    __satisfaccion = 'B'
    def __init__(self, edad, sexo, satisfaccion, prueba):
        self.__edad = edad
        self.__sexo = sexo
        self.__satisfaccion = satisfaccion
        self.__prueba = prueba
    def setEdad(self, edad):
        self.__edad = edad
    def getEdad(self):
        return self.__edad
    def getSexo(self):
        return self.__sexo
    def setSexo(self, sexo):
        self.__sexo = sexo
    def getSatisfaccion(self):
        return self.__satisfaccion
    def getPrueba(self):
        return self.__prueba
    def consultarEncuesta(self):
        print(f"Edad: {self.__edad} Sexo: {self.__sexo} Satisfaccion: {self.__satisfaccion} Prueba: {self.__prueba}")


def generarMostrar(n):
    encuestas = []
    opSexo = ['F', 'M']
    opPrueba = ['R', 'H', 'C']
    opSat = ['B', 'R', 'M']
    for i in range(n):
        edad = r.randint(18, 75)
        prueba = opPrueba[r.randint(0, 2)]
        sat = opSat[r.randint(0, 2)]
        sex = opSexo[r.randint(0, 1)]
        encuestas.append(Encunta(edad, sex, sat, prueba))
    for encuesta in encuestas:
        encuesta.consultarEncuesta()
    return encuestas
def cantidadAdultosMayores(encuestas):
    cont = 0
    for encuesta in encuestas:
        if encuesta.getEdad() >= 60:
            cont+=1
    print("Cantidad adultos mayores: ", cont)
def promedioPacientesCovid(encuestas):
    cont = suma = 0
    for encuesta in encuestas:
        if encuesta.getPrueba() == 'C':
            cont+=1
            suma += encuesta.getEdad()
    print(f"Promedio de edades de pacientes covid es : {suma / cont if cont > 0 else 0}")
def satisfaccionConMayorFrecuencia(encuestas):
    cB = cR = cM = 0
    for encuesta in encuestas: 
        if encuesta.getSatisfaccion() == 'B':
            cB+=1
        elif encuesta.getSatisfaccion() == 'R':
            cR+=1
        else:
            cM+=1
    print("Satisfaccion mas frecuente")
    if cB >= max(cR, cM): 
        print("Bueno")
    if cR >= max(cB, cM): 
        print("Regular")
    if cM >= max(cR, cB): 
        print("Malo")
def edadMujerJovenNoCovid(encuestas):
    minEdad = 100
    for encuesta in encuestas:
        if encuesta.getSexo() == 'F' and encuesta.getPrueba() != 'C' and minEdad > encuesta.getEdad():
            minEdad = encuesta.getEdad()
    if minEdad == 100:
        print("No existe mujer joven que no se realizo prueba covid")
    else:
        print(f"La edad de la mujer mas joven que no se realizo la prueba covid es {minEdad}")

n =-1
while not(n > 0 and n <= 40):
    n = int(input("Ingresar n : "))
encuestas = generarMostrar(n)
cantidadAdultosMayores(encuestas)
promedioPacientesCovid(encuestas)
satisfaccionConMayorFrecuencia(encuestas)
edadMujerJovenNoCovid(encuestas)

#EJERCICIO 4

import random as r
import pandas as pd
import matplotlib.pyplot as plt

n = 4
gastos = []
ingresos = []
meses = ['Enero', 'Febrero', 'Marzo', 'Abril']
for i in range(n):
    gastos.append(r.randint(1000, 4000))
    ingresos.append(r.randint(2000, 6000))
empresa = {
    'Gastos': gastos,
    'Ingresos': ingresos,
    'Meses': meses
    }
df = pd.DataFrame(empresa).set_index('Meses')
print(df)

df.plot(kind='line', title = 'Evolución de ingresos y gastos', ylim = (0))
plt.show()