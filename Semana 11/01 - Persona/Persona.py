import random
class Persona:
    __nombre = ""
    __edad = 0
    __sexo = "Masculino"
    __dni = ""
    __peso = 0
    __altura = 0
    def __init__(self, nombre, edad, sexo, dni, peso, altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__dni = dni
        self.__peso = peso
        self.__altura = altura
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getEdad(self):
        return self.__edad
    def setEdad(self, edad):
        self.__edad = edad
    def getSexo(self):
        return self.__sexo
    def setSexo(self, sexo):
        self.__nombre = sexo
    def getDNI(self):
        return self.__dni
    def setDNI(self, dni):
        self.__dni = dni
    def getPeso(self):
        return self.__peso
    def setPesoe(self, peso):
        self.__peso = peso
    def getAltura(self):
        return self.__altura
    def setAltura(self, altura):
        self.__altura = altura
    def getIMC(self):
        return self.__peso / (self.__altura**2)
    def analizarPesoIdeal(self):
        if self.getIMC() > 20: 
            return -1
        elif self.getIMC() < 25:
            return 0
        else:
            return 1
    def esMayorDeEdad(self):
        if(self.__edad >= 18):
            return True
        return False
    def generaDNI(self):#05000000
        #00123121
        for x in range(8):
            self.__dni += str(random.randint(0, 9))
    def toString(self):
        return "{} {} {} {} {} {}".format(self.__dni, self.__nombre,self.__sexo, self.__peso, self.__altura, self.__edad)
#class Estudiante(Persona): #Herencia
#    codigo = ""
