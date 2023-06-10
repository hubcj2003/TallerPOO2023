from Cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, dni, nombre, apellido, distrito, telefono, saldo):
        self._DNI = dni
        self._nombre = nombre
        self._apellido = apellido
        self._distrito = distrito
        self._telefono = telefono
        self._saldo= saldo
    def retirarSaldo(self, monto):
        self._saldo -= monto
    def ingresarSaldo(self, monto):
        self._saldo += monto
    def consultarCuenta(self):
        print(f"{self._DNI} {self._nombre} {self._apellido} {self._distrito} {self._telefono} {self._saldo}")
    def saldoNegativo(self):
        return self._saldo < 0