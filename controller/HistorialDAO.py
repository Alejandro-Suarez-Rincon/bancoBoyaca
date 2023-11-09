from controller.Conexion import Conexion


class HistorialDAO:
    def __init__(self):
        pass

    def crearHistorial(self, numeroCuenta, saldo, movimiento, fechaMovimiento, descripcion):
        try:
            conexion = Conexion()
            cdb = conexion.conectarBD()
            cursor = cdb.cursor()
            cursor.execute(
                f"INSERT INTO historial_cuenta (id_numero_cuenta, saldo, movimiento, fecha_movimeinto, descripcion)"
                f" VALUES (\"{numeroCuenta}\", \"{saldo}\", \"{movimiento}\", \"{fechaMovimiento}\", \"{descripcion}\")")
            cdb.commit()
            return True
        except Exception as e:
            return False

    def consultarHistorial(self, numeroCuenta):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(
            f"SELECT id_numero_cuenta, saldo, movimiento, fecha_movimiento, descripcion FROM historial_cuenta"
            f" WHERE id_numero_cuenta = \"{numeroCuenta}\"")
        buscar = cursor.fetchall()
        return buscar

    def buscarHistorial(self, numeroCuenta):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"SELECT id_numero_cuenta FROM historial_cuenta WHERE id_numero_cuenta = \"{numeroCuenta}\"")
        buscar = cursor.fetchone()

        if (buscar == numeroCuenta):
            return True
        return False
