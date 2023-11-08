import hashlib

from controller.UsuarioDAO import UsuarioDAO


class UsuarioDTO:
    def __init__(self, cedula, nombre, apellido, direccion, telefono, correo, contraeña, rol, idMunicipio,
                 fechaNacimiento, fechaExpedicion, estado):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._contraseña = contraeña
        self._rol = rol
        self._idMunicipio = idMunicipio
        self._fechaNacimiento = fechaNacimiento
        self._fechaExpedicion = fechaExpedicion
        self._estado = estado

    def autenticarUsuarios(self):
        contraseña = self.encriptarContraseña()
        self._contraseña = contraseña

        usuario = UsuarioDAO.consultarUsuario(self, self._cedula, self._contraseña)

        if (usuario == None):
            return None
        else:
            rolusuario = usuario[7]
            if (rolusuario == "usuario"):
                ## ir a vista usuario
                print("Usuario")
                return "USUARIO"
            elif (rolusuario == "administrador"):
                ## ir a Vista administrador
                print("Administrador")
                return "ADMINISTRADOR"
            else:
                ## no se encuentra el rol
                print("No se encuentra el rol")
                return None

    def crearUsuario(self):
        contraseña = self.encriptarContraseña()

        usuario = UsuarioDAO.crearUsuario(self, self._cedula, self._nombre, self._apellido, self._direccion,
                                          self._telefono,
                                          self._correo, contraseña, self._rol, self._fechaNacimiento,
                                          self._fechaExpedicion, self._estado, self._idMunicipio)

        if (usuario == True):
            return True
        else:
            return False
            # ir a usuario no se creo

    def deshavilitarUsuario(self):
        usuario = UsuarioDAO.deshabilitarUsuario(self, self._cedula, self._estado)
        if (usuario == True):
            print("Si")
        else:
            print("No")
        # ir a usuario no actualizado

    def actualizarUsuario(self):
        contraseña = self.encriptarContraseña()

        usuario = UsuarioDAO.actualizarUsuario(self, self._cedula, self._nombre, self._apellido, self._direccion,
                                               self._telefono,
                                               self._correo, contraseña, self._rol, self._fechaNacimiento,
                                               self._fechaExpedicion)

        if (usuario == True):
            # ir a usuario eliminado
            print("Si")
        else:
            # ir a usuario no actualizado
            print("No")

    def encriptarContraseña(self):
        contraseñaSTR = str(self._contraseña)
        contrasenaeEncriptada = hashlib.sha256(contraseñaSTR.encode()).hexdigest()
        return contrasenaeEncriptada
