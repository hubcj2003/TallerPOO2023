#from Persona import Persona as p
from Persona import *
#import Persona 
n = -1 
personas = []
while n < 0:
    n = int(input("Ingrese catidad de personas : "))
for x in range(n):
    edad = -1
    peso = -1.0
    altura = -1.0
    dni = ""
    sexo = ""
    nombre = input("Ingrese nombre : ")
    while len(dni) != 8:
        dni = input("Ingrese dni : ")
    while sexo != "Masculino" and sexo != "Femenino":
        sexo = input("Ingrese sexo : ")
        sexo.capitalize()
    while edad < 0:
        edad = int(input("Ingrese edad :  "))
    while peso < 0:
        peso = float(input("Ingrese peso :  "))  
    while altura < 0:
        altura = float(input("Ingrese altura :  "))
    persona = Persona(nombre, edad, sexo, dni, peso, altura)
    personas.append(persona)
for x in personas:
    print("Peso ideal : ", x.analizarPesoIdeal())
    print("Mayor de edad : ", x.esMayorDeEdad())

print("dni nombre sexo peso altura edad")
for x in personas:
    print(x.toString())




