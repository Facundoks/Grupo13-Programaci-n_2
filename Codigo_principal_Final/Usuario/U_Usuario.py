
from csv import reader

from Monitoreo.M_Anses import Anses
from Monitoreo.M_ABM import ABM


class Usuario:
    @staticmethod
    def checkLogin(login, tipo):
        a = Usuario()
        if a.checkNombre(login, tipo):
            return login
        elif a.checkCuil(login, tipo):
            return login
        elif a.checkTelefono(login, tipo):
            return login

    @staticmethod
    def checkNombre(nombre, tipo):
        nombre = str(nombre)
        return Anses(tipo).confirmarNombre(nombre)

    @staticmethod
    def checkCuil(cuil, tipo):
        cuil = str(cuil)
        return Anses(tipo).confirmarCuil(cuil)

    @staticmethod
    def checkTelefono(telef, tipo):
        telef = str(telef)
        return Anses(tipo).confirmarTelef(telef)

    @staticmethod
    def getInfo(tipo_usuario, dato_ingreso):
        ciu = tipo_usuario.lower()
        with open(f"../Database/DB_{ciu}.csv", "r") as lector:
            leer = reader(lector)
            for linea in leer:
                for elemento in linea:
                    if elemento == dato_ingreso:
                        info_usuario = linea
                        del info_usuario[1]
                        return info_usuario

    @staticmethod
    def registrar(nombre, contra, cuil, telef, x, y):
        a = Usuario().checkNombre(nombre, "ciudadano")
        b = Usuario().checkCuil(cuil, "ciudadano")
        c = Usuario().checkTelefono(telef, "ciudadano")
        if not a and b and c:
            ABM().agregarUsuario(nombre, contra, cuil, telef, x, y)

    @staticmethod
    def ingresarAdmin(tipo_ingreso, dato_ingreso, contra):
        return Usuario().ingresar("Admin", tipo_ingreso, dato_ingreso, contra)

    @staticmethod
    def ingresarCiudadano(tipo_ingreso, dato_ingreso, contra):
        return Usuario().ingresar("Ciudadano", tipo_ingreso, dato_ingreso, contra)

    @staticmethod
    def ingresar(tipo_usuario, tipo_ingreso, dato_ingreso, contra):
        check = Usuario().checkLogin(dato_ingreso, tipo_usuario)
        cofirmacion_contra = Anses(tipo_usuario).confirmarContra(tipo_ingreso, dato_ingreso, contra)
        if tipo_ingreso == "Nombre" or "Cuil" or "Teléfono":
            if not ABM().getBlock(tipo_usuario, tipo_ingreso, dato_ingreso):
                if check and cofirmacion_contra:
                    print("Ingreso completo")
                else:
                    raise ValueError("Contraseña incorrecta")
            else:
                raise ValueError("Usuario bloqueado")
        else:
            raise ValueError("El tipo de ingreso es incorrecto")


