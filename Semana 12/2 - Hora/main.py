class Hora:
    __hora = 0
    __minuto = 0
    __segundo = 0
    def __init__(self, hora, minuto, segundo):
        self.setHora(hora, minuto, segundo)
    def setHora(self, hora, minuto, segundo):
        self.__hora = hora if hora >= 0 and hora <= 23 else 0
        if minuto >= 0 and minuto < 60:
            self.__minuto = minuto
        else:
            self.__minuto = 0
        self.__segundo = segundo if segundo >= 0 and segundo < 60 else 0
    def getHora(self):
        return [self.__hora, self.__minuto, self.__segundo]
    def imprimirHora(self):
        print("{}:{}:{}".format(self.__hora, self.__minuto, self.__segundo))
    def incrementarSegundo(self):
        segundosTotales = self.transformarASegundos() + 1
        self.__hora = segundosTotales //3600
        segundosTotales = segundosTotales % 3600
        self.__minuto = segundosTotales //60
        self.__segundo = segundosTotales % 60
    def cuantoFaltaParaFinalDia(self):
        segundosTotales = self.transformarASegundos()
        segundosFaltantes = 24 * 3600 - segundosTotales
        hora = segundosFaltantes //3600
        segundosFaltantes = segundosFaltantes % 3600
        minuto = segundosFaltantes //60
        segundo = segundosFaltantes % 60
        print(f"Para el final del dia faltan {hora}:{minuto}:{segundo}")
    def transformarASegundos(self):
        return self.__hora * 3600 + self.__minuto * 60 + self.__segundo 

def ingresar(lista):
    hora = -2
    while hora != -1:
        hora = -2
        while not (hora >= 0 and hora <= 23 or hora == -1):
            hora = int(input("Ingrese hora: "))
        if hora != -1:
            minuto = -1
            while not (minuto >= 0 and minuto <= 59):
                minuto = int(input("Ingrese minuto: "))
            segundo = -1
            while not (segundo >= 0 and segundo <= 59):
                segundo = int(input("Ingrese segundo: "))
            lista.append(Hora(hora, minuto, segundo))
def incrementar(lista):
    for hora in lista:
        hora.incrementarSegundo()
        hora.imprimirHora()
def diferenciaHoraria(lista):
    listaSegundos = []
    for hora in lista:
        listaSegundos.append(hora.transformarASegundos())
    mayorS = max(listaSegundos)
    menorS = min(listaSegundos)
    segundosDiferencia = mayorS - menorS
    hora = segundosDiferencia //3600
    segundosDiferencia = segundosDiferencia % 3600
    minuto = segundosDiferencia //60
    segundo = segundosDiferencia % 60
    print(f"De la mayor hora a la menor hora hay {hora}:{minuto}:{segundo} de diferencia")

horas = []
ingresar(horas)
incrementar(horas)
diferenciaHoraria(horas)
for hora in horas:
    hora.cuantoFaltaParaFinalDia()

