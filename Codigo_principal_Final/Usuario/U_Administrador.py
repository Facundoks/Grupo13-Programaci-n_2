from Monitoreo.M_ABM import *
from Usuario.U_Usuario import Usuario


class Admin(Usuario):
    def __init__(self, cuil, telef, contra):
        self.cuil = cuil
        self.telef = telef
        self.contra = contra
        self.ingresarAdmin("Cuil", self.cuil, self.contra)

    @staticmethod
    def cambiarEstado(tipo, estado):
        df = pd.read_csv("../Database/DB_evento.csv")
        df.head(5)
        df.loc[df["Tipo"] == tipo, "Estado"] = estado
        df.to_csv("../Database/DB_evento.csv", index=False)


    def darAlta(self, tipo):
        self.cambiarEstado(tipo, "Alta")

    def darBaja(self, tipo):
        self.cambiarEstado(tipo, "Baja")

    @staticmethod
    def Bloquear(usuario):
        df = pd.read_csv("../Database/DB_ciudadano.csv")
        df.head(6)
        # Busco el nombre y cambio el cvs a bloqueado
        df.loc[df["Nombre"] == usuario, "Bloqueado"] = "y"
        df.to_csv("../Database/DB_ciudadano.csv", index=False)

    @staticmethod
    def Desbloquear(usuario):
        df = pd.read_csv("../Database/DB_ciudadano.csv")
        df.head(6)
        df.loc[df["Nombre"] == usuario, "Bloqueado"] = "n"
        df.to_csv("../Database/DB_ciudadano.csv", index=False)
