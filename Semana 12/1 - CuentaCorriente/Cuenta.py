class Cuenta:
    def __init__(self):
        self._DNI = ""
        self._nombre = ""
        self._apellido = ""
        self._distrito = ""
        self._telefono = ""
        self._saldo= 0.0
    def getDNI(self):
        return self._DNI
    def getnombre(self):
        return self._nombre
    def getapellido(self):
        return self._apellido
    def getdistrito(self):
        return self._distrito
    def gettelefono(self):
        return self._telefono
    def getsaldo(self):
        return self._saldo
    def setDNI(self, valor):
        self._DNI = valor
    def setnombre(self, valor):
        self._nombre = valor
    def setapellido(self, valor):
        self._apellido = valor
    def setdistrito(self, valor):
        self._distrito = valor
    def settelefono(self, valor):
        self._telefono = valor
    def setsaldo(self, valor):
        self._saldo = valor