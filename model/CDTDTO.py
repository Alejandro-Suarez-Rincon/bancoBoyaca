from controller.CDTDAO import CDTDAO
from controller.CuentaDAO import CuentaDAO
from model.CuentaDTO import CuentaDTO


class CDTDTO(CuentaDTO):
    def __init__(self, clausula, retencion, fechaFinalizacion, aproxInteres, numeroCuenta, saldo, fechaApertura,
                 tasaInteres, ultimoMovimiento, idSucursal, idUsuario):

        CuentaDTO.__init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento, idSucursal,
                           idUsuario)

        self._clausula = clausula
        self._retencion = retencion
        self._fechaFinalizacion = fechaFinalizacion
        self._aproxInteres = aproxInteres

    def crearCDT(self):
        cuenta = CuentaDAO.crearCuenta(self, self._numeroCuenta, self._idSucursal, self._saldo, self._fechaApertura,
                                       self._tasaInteres, self._ultimoMovimiento, self._idUsuario)

        if (cuenta == True):
            CDT = CDTDAO.crearCDT(self, self._numeroCuenta, self._clausula, self._retencion, self._fechaFinalizacion,
                                  self._aproxInteres)
            if (CDT == True):
                print(CDT)
                return True
            else:
                print("No")
        else:
            print("No cuenta")

    def consultarCDT(self):
        CDT = CDTDAO.buscarCDT(self, self._numeroCuenta)
        if(CDT == []):
            return False
        else:
            return CDT


    def calcularSinGuardarCDT(self):
        pass

    def calculoCDT(self):
        pass
