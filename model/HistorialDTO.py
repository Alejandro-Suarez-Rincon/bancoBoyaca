import datetime
from controller.HistorialDAO import HistorialDAO

class HistorialDTO:
    def __init__(self, numeroCuenta, saldo, movimiento, fechaMovimiento, descripcion):
        self._numeroCuenta = numeroCuenta
        self._saldo = saldo
        self._movimiento = movimiento
        self._fechaMovimiento = fechaMovimiento
        self._descripcion = descripcion

    def crearHistorial(self):
        fechaActual = datetime.datetime.now()
        historial = HistorialDAO.crearHistorial(self, self._numeroCuenta, self._saldo, self._movimiento, self._movimiento,
                                                fechaActual, self._descripcion)
        return historial

    def consultarHistorial(self):
        hisotrial = HistorialDAO.consultarHistorial(self, self._numeroCuenta)
        return hisotrial
