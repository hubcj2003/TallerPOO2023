#from Contrasenia import Contrasenia
#import random
#import csv

#n = random.randint(6, 12)
#contrasenias = []
#esSegura = []
#for x in range(n):
#    contrasenia = Contrasenia(random.randint(8, 12))
#    contrasenia.generarContrasena()
#    contrasenias.append(contrasenia.getContrasenia())
#    esSegura.append(contrasenia.esSeguro())
#for x in range(n):
#    print( x, "\t", contrasenias[x], "\t", esSegura[x])

from Contrasenia import Contrasenia
import random
import csv
contrasenias = []
esSegura = []

#file = open("archivo.csv") 
with open("archivo.csv") as file:
    datos = csv.DictReader(file, delimiter = ";")
    for x in datos:
        contrasenia = Contrasenia(x['Contrasenia'])
        contrasenias.append(contrasenia.getContrasenia())
        esSegura.append(contrasenia.esSeguro())
for x in range(len(esSegura)):
        print( x, "\t", contrasenias[x], "\t", esSegura[x])
