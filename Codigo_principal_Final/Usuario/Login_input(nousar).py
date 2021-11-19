from Monitoreo.M_ABM import *
from Monitoreo.M_Anses import *

class Usuario:
    tipo_usuario = ()

    @classmethod
    def checkNombre(cls, nombre, tipo):
        return M_Anses(tipo).confirmarNombre(nombre)

    @classmethod
    def checkCuil(cls, cuil, tipo):
        return M_Anses(tipo).confirmarCuil(cuil)

    @classmethod
    def checkTelefono(cls, telef, tipo):
        return M_Anses(tipo).confirmarTelef(telef)



    def enterNombre(self, valor, tipo):
        nombre = input("Ingresar un nombre de usuario: ")
        while Usuario().checkNombre(nombre, tipo) == valor:
            nombre = input("Nombre de usuario incorrecto. Ingresar un nombre de usuario: ")
        return nombre

    def enterContra(self):
        contra = input("Ingresar una contraseña: ")
        contra2 = input("Vuelva a ingresar su contraseña: ")
        while contra != contra2:
            contra = input("Contraseñas distintas. Ingrese nuevamente su contraseña: ")
            contra2 = input("Vuelva a ingresar su contraseña: ")
        return contra

    def enterCuil(self, valor, tipo):
        cuil = input("Ingrese su CUIL: ")
        while Usuario().checkTelefono(valor, tipo) == valor:
            cuil = input("CUIL incorrecto. Ingrese su CUIL: ")
        return cuil

    def enterTelefono(self):
        telef = input("Ingrese su número de teléfono: ")
        while Usuario().checkTelefono(telef, "ciudadano") == telef:
            telef = input("Número de teléfono incorrecto. Ingrese su número de teléfono: ")
        return telef



    def registrar(self):
        nombre = Usuario().enterNombre(True, "ciudadano")
        contra = Usuario().enterContra()
        cuil = Usuario().enterCuil(True, "ciudadano")
        telef = Usuario().enterTelef(True, "ciudadano")
        zona = input("Ingrese su zona actual: ")

        ABM().agregarUsuario(nombre, contra, cuil, telef, zona)


    def ingresar_admin(self, login, contra):
        if ingreso == "u":
            nombre = Usuario().enterNombre(False, "admin")
            contra = Usuario().enterContra()
                if nombre and contra:
                    print("Ingreso completo, bienvenido")
            elif ingreso == "t":
                telef = Usuario().enterTelef(False, "admin")
                contra = Usuario().enterContra()
                if telef and contra:
                    print("Ingreso completo, bienvenido")
            elif ingreso == "c":
                cuil = Usuario().enterCuil(False, "admin")
                contra = Usuario().enterContra()
                if cuil and contra:
                    print("Ingreso completo, bienvenido")
            tipo_usuario = ("administrador")
        if ingreso == "u":
                nombre = Usuario().enterNombre(False, "admin")
                contra = Usuario().enterContra()
                if nombre and contra:
                    print("Ingreso completo, bienvenido")
        elif ingreso == "t":
            telef = Usuario().enterTelef(False, "admin")
            contra = Usuario().enterContra()
            if telef and contra:
                print("Ingreso completo, bienvenido")
        elif ingreso == "c":
            cuil = Usuario().enterCuil(False, "admin")
            contra = Usuario().enterContra()
            if cuil and contra:
                print("Ingreso completo, bienvenido")
        self.tipo_usuario = ("administrador")



    def ingresar_ciudadano(self):
        if ingreso == "u":
            nombre = Usuario().enterNombre(False, "ciudadano")
            contra = Usuario().enterContra()
            cof_contra = M_Anses("ciudadano").confirmarContra("Nombre", nombre, contra)
            if not ABM().getBlock("Nombre", nombre):
                if nombre and contra and cof_contra:
                    print("Ingreso completo, bienvenido")
                else:
                    print("Contraseña incorrecta")
            else:
                raise ValueError("Usuario bloqueado, no puede ingresar")

        elif ingreso == "t":
            telef = Usuario().enterTelef(False, "ciudadano")
            contra = Usuario().enterContra()
            if ABM().getBlock("Teléfono", telef):
                if telef and contra:
                    print("Ingreso completo, bienvenido")
            else:
                raise ValueError("Usuario bloqueado, no puede ingresar")

            elif ingreso == "c":
                cuil = Usuario().enterCuil(False, "ciudadano")
                contra = Usuario().enterContra()
                if ABM().getBlock("Cuil", cuil):
                    if cuil and contra:
                        print("Ingreso completo, bienvenido")
                else:
                    raise ValueError("Usuario bloqueado, no puede ingresar")
            self.tipo_usuario = ("ciudadano")



    def ingresar(self, tipo_usuario, tipo_ingreso):
        tipo_ing = f"enter{tipo_ingreso.lower().title()}"
        ingreso = Usuario().tipo_ing()
        ingreso = input("¿Desea ingresar por usuario (u), teléfono (t), o CUIL (c)? ")
        if ingreso == "u":
            nombre = Usuario().enterNombre(False, "ciudadano")
            contra = Usuario().enterContra()
            cof_contra = M_Anses("ciudadano").confirmarContra("Nombre", nombre, contra)
            if not ABM().getBlock("Nombre", nombre):
                if nombre and contra and cof_contra:
                    print("Ingreso completo, bienvenido")
                else:
                    print("Contraseña incorrecta")
            else:
                raise ValueError("Usuario bloqueado, no puede ingresar")





Usuario().ingresar()
