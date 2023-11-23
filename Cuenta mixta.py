from CuentaAhorro import CuentaAhorro
from CuentaCorriente import CuentaCorriente

#CARLOS ALEXIS ASENCIO MADESCO
class Cuentamixta(CuentaAhorro, CuentaCorriente):
    def __init__(self, numero, nombre_propietario, saldo, interes, tieneChequera, limite:float=None, bono:float=None):
        CuentaAhorro.__init__(self, numero, nombre_propietario, saldo, interes)
        CuentaCorriente.__init__(self, numero, nombre_propietario, saldo, tieneChequera)
        self._limite = limite
        self._bono = bono
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, cantidad):
        self._limite = cantidad

    @property
    def bono(self):
        return self._bono

    @bono.setter
    def bono(self, cantidad):
        self._bono = cantidad


#EJEMPLO DE USO
if __name__ == '__main__':
    cuenta_mixta = Cuentamixta(numero='087485748', nombre_propietario='ALEXIS ASENCIO',saldo=9000, interes=0.06, tieneChequera=800, limite=40000, bono=8000)
    print("Saldo inicial de la cuenta mixta:", cuenta_mixta.saldo)
    print("Límite de la cuenta mixta:", cuenta_mixta._limite)
    print("Bono de la cuenta mixta:", cuenta_mixta._bono)

    cuenta_mixta.credito(500)
    print("Saldo después del depósito:", cuenta_mixta.saldo)

    cuenta_mixta.debito(1200)
    print("Saldo después del retiro:", cuenta_mixta.saldo)