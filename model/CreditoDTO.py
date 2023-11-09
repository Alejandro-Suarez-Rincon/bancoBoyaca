from controller.CreditoDAO import CreditoDAO
from controller.CuentaDAO import CuentaDAO
from model.CuentaDTO import CuentaDTO


class CreditoDTO(CuentaDTO):
    def __init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento, idSucursal, idUsuario):
        CuentaDTO.__init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento, idSucursal,
                           idUsuario)

    def crearCredito(self):
        cuenta = CuentaDAO.crearCuenta(self, self._numeroCuenta, self._idSucursal, self._saldo, self._fechaApertura,
                                       self._tasaInteres, self._ultimoMovimiento, self._idUsuario)
        if (cuenta):
            credito = CreditoDAO.crearCorriente(self, self._numeroCuenta)
            if (credito):
                # Credito creado correctamente
                print("Si")
            else:
                print("No")
        else:
            # no se creo ninguna cuenta
            print("No hay cuentas creadas")

    def buscarCredito(self):
        credito = CreditoDAO.buscarCredito(self, self._numeroCuenta)
        if (credito == False):
            # No se encuentra credito
            print("No")
        else:
            # Imprimir informacion
            print(credito)

    def consultarCredito(self):
        cuenta = CuentaDAO.consultarCuenta(self, self._numeroCuenta)
        if (cuenta == None):
            # No se encuentra la ceunta
            return False
        else:
            # Imprimir datos
            return cuenta
