import os

import uvicorn
from fastapi import FastAPI, APIRouter, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from model.UsuarioDTO import UsuarioDTO
from view.index import (principalView, loginView, indexView, register_User, update_User, disable_User,
                        emergenteRegisterUser,
                        register_Sucursal,
                        update_Sucursal, disable_Sucursal, register_CDT, emergenteRegisterCDT, register_Credito,
                        emergenteRegisterCredito, register_Corriente, emergenteRegisterCorriente, consult_Historial)

STATIC_PATH = os.path.abspath(os.path.join(os.getcwd(), "view/static"))
print(STATIC_PATH)


class Control:
    def __init__(self):
        self.app = FastAPI()
        self.router = APIRouter()

    def principal(self, request: Request):
        return principalView(request)

    def index(self, request: Request):
        return indexView(request)

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
                return RedirectResponse("/index", status_code=303)
            elif (usuario == "ADMINISTRADOR"):
                ## debe tener una vista administrador diferente a la del usuario "index"
                pass
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


    def routers(self):
        self.router.add_api_route("/", self.principal)
        self.router.add_api_route("/login", self.login, methods=["GET", "POST"])
        self.router.add_api_route("/index", self.index)
        self.router.add_api_route("/registro", self.registrarUsuario, methods=["GET", "POST"])

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
