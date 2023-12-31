import os

import uvicorn
from fastapi import FastAPI, APIRouter, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from model.CreditoDTO import CreditoDTO
from model.CDTDTO import CDTDTO
from model.CuentaDTO import CuentaDTO
from model.HistorialDTO import HistorialDTO
from model.UsuarioDTO import UsuarioDTO
from view.index import (principalView, loginView, register_User, consultarCDT, consultarCDT2,
                        principalViewUser, consult_Historial, consultHistorial2, consultCredito2, consultCuenta2,
                        contactanos, principalViewAdmin, indexView, register_Credito, update_User,
                        disable_User, emergenteRegisterUser, register_Sucursal, update_Sucursal, updateSucursal2,
                        disable_Sucursal, register_CDT, emergenteRegisterCDT, emergenteRegisterCredito, register_Cuenta,
                        emergenteRegisterCorriente, information, consultCuenta)

STATIC_PATH = os.path.abspath(os.path.join(os.getcwd(), "view/static"))
print(STATIC_PATH)


class Control:
    def __init__(self):
        self.app = FastAPI()
        self.router = APIRouter()

    def principal(self, request: Request):
        return principalView(request)

    def indexUsuario(self, request: Request):
        return principalViewUser(request)

    async def login(self, request: Request):

        if (request.method == "POST"):
            form_data = await request.form()
            id = form_data.get("id")
            contraseña = form_data.get("contraseña")

            objeto = UsuarioDTO(id, None, None, None, None, None, contraseña,
                                None, None, None, None, None)
            usuario = objeto.autenticarUsuarios()

            if (usuario == None):
                return loginView(request)
            elif (usuario == "USUARIO"):
                return RedirectResponse("/indexUsuario", status_code=303)
            elif (usuario == "ADMINISTRADOR"):
                ## debe tener una vista administrador diferente a la del usuario "index"
                return RedirectResponse("/indexAdmin", status_code=303)
        return loginView(request)

    async def registrarUsuario(self, request: Request):
        ## Buscar ciudad
        municipioEnviar = "Duitama"

        if (request.method == "POST"):
            form_data = await request.form()
            cedula = form_data.get("cedula")
            nombre = form_data.get("nombre")
            apellido = form_data.get("apellidos")
            direccion = form_data.get("direccion")
            telefono = form_data.get("telefono")
            correo = form_data.get("correo")
            rol = "usuario"
            contraseña = form_data.get("contrasena")
            fechaNacimiento = form_data.get("fechaNacimineto")
            fechaExpedicion = form_data.get("fechaExpedicion")
            estado = form_data.get("estado")
            municipio = 15238

            usuario = UsuarioDTO(cedula, nombre, apellido, direccion, telefono, correo, contraseña, rol, municipio,
                                 fechaNacimiento, fechaExpedicion, estado)
            respuesta = usuario.crearUsuario()

            if (respuesta):
                return RedirectResponse("/login", status_code=303)
            else:
                return RedirectResponse("/", status_code=303)

        return register_User(request, municipioEnviar)

    ## CUENTAS
    async def consultarCDT(self, request: Request):
        if (request.method == "POST"):
            form_data = await request.form()
            numeroCuenta = form_data.get("numeroCuenta")

            cdt = CDTDTO(None, None, None, None, numeroCuenta, None,
                         None, None, None, None, None)

            consulta = cdt.consultarCDT()
            if (consulta):
                return RedirectResponse("/consultarCDT2", status_code=303)
            else:
                return consultarCDT(request)

        return consultarCDT(request)

    def consultarCDT2(self, request: Request):
        return consultarCDT2(request)

    def cosultarCredito2(self, request:Request):
        return consultCredito2(request)

    async def consultarCuenta(self, request:Request):
        if (request.method == "POST"):
            form_data = await request.form()
            numeroCuenta = form_data.get("numeroCuenta")

            cuenta = CreditoDTO(numeroCuenta, None, None, None, None,
                                None, None)

            consulta = cuenta.consultarCredito()
            if (consulta == False):
                return consultCuenta(request)
            else:
                return RedirectResponse("/consultarCuenta2", status_code=303)

        return consultCuenta(request)

    def consultarCuenta2(self, request:Request):
        return consultCuenta2(request)

    def consultarHistorial(self, request:Request):
        numeroCuenta = 300
        historial = HistorialDTO(numeroCuenta, None, None, None, None)
        h = historial.consultarHistorial()

        if (h == []):
            return RedirectResponse("/indexUsuario", status_code=303)
        else:
            id = h[0]
            saldo = h[1]
            movimiento = [2]
            fechaMovimeinto = [3]
            descripcion = [4]


        return consult_Historial(request, id, saldo, movimiento, fechaMovimeinto, descripcion)

    def informacionBancaria(self, request:Request):
        return information(request)


    def contactanos(self, request:Request):
        return contactanos(request)

    def routers(self):
        self.router.add_api_route("/", self.principal)
        self.router.add_api_route("/login", self.login, methods=["GET", "POST"])
        self.router.add_api_route("/indexUsuario", self.indexUsuario)
        self.router.add_api_route("/registro", self.registrarUsuario, methods=["GET", "POST"])
        self.router.add_api_route("/consultarCDT", self.consultarCDT, methods=["GET", "POST"])
        self.router.add_api_route("/consultarCDT2", self.consultarCDT2, methods=["GET", "POST"])
        self.router.add_api_route("/consultarCredito2", self.cosultarCredito2, methods=["GET", "POST"])
        self.router.add_api_route("/consultarCuenta", self.consultarCuenta, methods=["GET", "POST"])
        self.router.add_api_route("/consultarCuenta2", self.consultarCuenta2, methods=["GET", "POST"])
        self.router.add_api_route("/consultarHistorial", self.consultarHistorial , methods=["GET", "POST"])
        self.router.add_api_route("/informacionBancaria", self.informacionBancaria, methods=["GET", "POST"])
        self.router.add_api_route("/contactanos", self.contactanos, methods=["GET", "POST"])



    # Don't modify this code only routers
    def web_config(self):
        self.app.mount(
            "/static",
            StaticFiles(directory=STATIC_PATH),
            name="static"
        )
        self.routers()
        self.app.include_router(self.router)

    def run(self):
        self.web_config()
        uvicorn.run(self.app, host="127.0.0.1", port=5000)
