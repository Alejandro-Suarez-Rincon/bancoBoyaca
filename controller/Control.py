import os

import uvicorn
from fastapi import FastAPI, APIRouter, Request
from fastapi.staticfiles import StaticFiles
from view.index import (principalView, loginView, register_User, update_User, disable_User, emergenteRegisterUser,
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

    def login(self, request: Request):
        return loginView(request)

    def routers(self):
        self.router.add_api_route("/", self.principal)
        self.router.add_api_route("/login", self.login, methods=["GET", "POST"])

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
