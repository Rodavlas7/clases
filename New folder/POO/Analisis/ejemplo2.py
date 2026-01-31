class CuentaBancaria:
    def __init__(self, numero, titular, tipo, fecha_apertura, saldo_inicial):
        self.__Numero = numero
        self.__Titular = titular
        self.__Tipo = tipo
        self.__FechaApertura = fecha_apertura
        self.__Saldo = saldo_inicial
        self.__Activa = True

    def ConsultarSaldo(self):
        return self.__Saldo

    def Depositar(self, monto):
        if self.__Activa and monto > 0:
            self.__Saldo += monto
            print("Depósito exitoso.")
            return True
        return False

    def Retirar(self, monto):
        if self.__Activa and monto > 0 and monto <= self.__Saldo:
            self.__Saldo = self.__Saldo - monto
            print("Retiro exitoso.")
            return True
        print("No se puede realizar el retiro.")
        return False

    def CancelarCuenta(self):
        if self.__Saldo == 0:
            self.__Activa = False
            print("Cuenta cancelada exitosamente.")
            return True
        print("No se puede cancelar la cuenta. El saldo debe ser cero.")
        return False

    def ObtenerTitular(self):
        return self.__Titular

    def ObtenerTipo(self):
        return self.__Tipo

    def EstaActiva(self):
        return self.__Activa
    
    def ObtenerNumero(self):
        return self.__Numero



class Banco:
    def __init__(self):
        self.__Cuentas = []
        self.__SiguienteNumero = 1

    def AbrirCuenta(self, titular, tipo, fecha_apertura, saldo_inicial):
        if saldo_inicial < 0:
            return None

        for cuenta in self.__Cuentas:
            if cuenta.ObtenerTitular() == titular and cuenta.ObtenerTipo() == tipo:
                return None

        nueva_cuenta = CuentaBancaria(
            self.__SiguienteNumero,
            titular,
            tipo,
            fecha_apertura,
            saldo_inicial
        )

        self.__Cuentas.append(nueva_cuenta)
        self.__SiguienteNumero += 1
        return nueva_cuenta


banco = Banco()

cuenta1 = banco.AbrirCuenta("Monserrat Anguiano", "Ahorro", "2026-07-27", 500)
cuenta2 = banco.AbrirCuenta("Monserrat Anguiano", "Corriente", "2026-07-27", 1000)
cuenta3 = banco.AbrirCuenta("Monserrat Anguiano", "Ahorro", "2026-07-27", 300)  # esta no

print(cuenta1.ConsultarSaldo()) 
cuenta1.Depositar(1000)
print(cuenta1.ConsultarSaldo())  
cuenta1.Retirar(900)
print(cuenta1.ConsultarSaldo())  

cuenta1.CancelarCuenta()
cuenta1.Retirar(600)
cuenta1.CancelarCuenta()

print(cuenta3) 
