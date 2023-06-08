import random

class Contrasenia:
    __longitud = 8
    __contrasenia =  ""
    #def __init__ (self, longitud):
    #    self.__longitud = longitud
    def __init__ (self, contrasenia):
        self.__longitud = len(contrasenia)
        self.__contrasenia = contrasenia
    def generarContrasena(self):
        for x in range(self.__longitud):
            r = random.randint(1,3)
            if  r == 1:
                self.__contrasenia += chr(random.randint(65,90))
            elif r == 2:
                self.__contrasenia += chr(random.randint(97,122))
            else:
                self.__contrasenia += chr(random.randint(48,57))
    def esSeguro(self):
        #cMay = cMin =  cNum = 0 
        cMay , cMin, cNum = 0, 0, 0
        for x in self.__contrasenia: 
            if x.isupper(): #Retorna True si el caracter analizado es mayuscula
                cMay+=1
            elif x.islower(): #Retorna True si el caracter analizado es minuscula
                cMin+=1
            else:
                cNum+=1
        #if cMay > 2 and cMin > 1 and cNum > 5: return True;
        #return False
        return cMay > 2 and cMin > 1 and cNum > 5
    def getContrasenia(self):
        return self.__contrasenia
    def setContrasenia(self, contrasenia):
        self.__contrasenia = contrasenia
    def getLongitud(self):
        return self.__longitud
    def setLongitud(self, longitud):
        self.__longitud = longitud

