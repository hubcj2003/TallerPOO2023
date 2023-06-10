from CuentaCorriente import CuentaCorriente

class Controlador:
    cuentas = []
    def ingresarCuentas(self):
        dni = " "
        while dni != "":
            dni = " "
            while not(len(dni) == 8 or dni == ""):
                dni = input("Ingrese dni : ")
            if dni != "":
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese apellido: ")
                distrito = input("Ingrese distrito: ")
                telefono = input("Ingrese telefono: ")
                saldo = float(input("Ingrese saldo: "))
                self.cuentas.append(CuentaCorriente(dni, nombre, apellido, distrito, telefono, saldo))
    def transferencia(self):
        dniOrigen = ""
        while len(dniOrigen) != 8:
            dniOrigen = input("Ingrese dni origen : ")
        dniDestino = ""
        while len(dniDestino) != 8:
            dniDestino = input("Ingrese dni destino : ")
        monto = 0
        while monto <= 0:
            monto =float(input("Ingrese monto : "))
        for cuenta in self.cuentas:
            if cuenta.getDNI() == dniOrigen:
                cuenta.retirarSaldo(monto)
            if cuenta.getDNI() == dniDestino:
                cuenta.ingresarSaldo(monto)
        for cuenta in self.cuentas:
            cuenta.consultarCuenta()
    def saldoPromedio(self):
        suma = c = 0
        distrito = input("Ingrese distrito : ")
        for cuenta in self.cuentas:
            if cuenta.getdistrito() == distrito:
                suma+= cuenta.getsaldo()
                c+=1
        print("El saldo promedio es : ", suma / c if c != 0 else 0)
    def buscarPersonaPorInicialApellido(self):
        inicial = input("Ingrese inicial del apellido : ")
        for cuenta in self.cuentas:
            if cuenta.getapellido()[0] == inicial:
                cuenta.consultarCuenta()
    def mayorSaldoCuentas(self):
        print("Cuenta con mayor saldo : ")
        mayorSaldo = max(self.cuentas, key=lambda cuenta: cuenta._saldo)
        for cuenta in self.cuentas:
            if cuenta.getsaldo() == mayorSaldo.getsaldo():
                cuenta.consultarCuenta()