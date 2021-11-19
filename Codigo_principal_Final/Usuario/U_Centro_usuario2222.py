
from csv import reader

from Monitoreo.M_Anses import Anses
from Monitoreo.M_ABM import ABM
from U_Administrador import Admin
from U_Ciudadano import Ciudadano


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
        return Anses(tipo).confirmarNombre(nombre)

    @staticmethod
    def checkCuil(cuil, tipo):
        return Anses(tipo).confirmarCuil(cuil)

    @staticmethod
    def checkTelefono(telef, tipo):
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
    def registrar(nombre, contra, cuil, telef, zona):
        a = Usuario().checkNombre(nombre, "ciudadano")
        b = Usuario().checkCuil(cuil, "ciudadano")
        c = Usuario().checkTelefono(telef, "ciudadano")
        if not a and b and c:
            ABM().agregarUsuario(nombre, contra, cuil, telef, zona)

    @staticmethod
    def ingresarAdmin(tipo_ingreso, dato_ingreso, contra):
        return Usuario().ingresar("Admin", tipo_ingreso, dato_ingreso, contra)


    @staticmethod
    def ingresarCiudadano(tipo_ingreso, dato_ingreso, contra):
        return Usuario().ingresar("Ciudadano", tipo_ingreso, dato_ingreso, contra)

    @staticmethod
    def ingresar(tipo_usuario, tipo_ingreso, dato_ingreso, contra):
        tipo_usuario = tipo_usuario.lower()
        check = Usuario().checkLogin(tipo_ingreso, tipo_usuario)
        cofirmacion_contra = Anses(tipo_usuario).confirmarContra(tipo_ingreso, dato_ingreso, contra)
        tipo_ingreso = tipo_ingreso.title().strip()
        if tipo_ingreso == "Nombre" or "Cuil" or "Teléfono":
            if not ABM().getBlock(tipo_usuario, tipo_ingreso, dato_ingreso):
                if check and contra and cofirmacion_contra:
                    lista_usuario = Usuario().getInfo(tipo_usuario, dato_ingreso)
                    solo_cuil_telef = lista_usuario[1:3]
                    cuil = solo_cuil_telef[0]
                    telef = solo_cuil_telef[1]
                    if tipo_ingreso == "Admin":
                        user_adm = Admin(cuil, telef)
                        return user_adm
                    elif tipo_ingreso == "Ciudadano":
                        user_ciu = Ciudadano(cuil, telef)
                        return user_ciu
                else:
                    print("Contraseña incorrecta")
            else:
                raise ValueError("Usuario bloqueado")
        else:
            raise ValueError("El tipo de ingreso es incorrecto")


facu = Usuario.ingresarCiudadano("Nombre", "Facu", "mimama")
a = Usuario.getInfo("Ciudadano", "Facu")
okse = Usuario.ingresarCiudadano("Nombre", "Okse", "ayuda")
b = Usuario.getInfo("Ciudadano", "Okse")
info2 = [a] + [b]
Facundo = Usuario().ingresarAdmin("Nombre", "Facundo", "patas")
h = Admin.crearEvento(Facundo, "Plaza", "c", "3")

print(info2)
ciu = Ciudadano("ads", "df")
asd = ciu.vincular_evento(h, info2)
