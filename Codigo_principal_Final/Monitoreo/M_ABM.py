from Monitoreo import M_Anses
# pip3 install pandas para que funciones la libreria
import csv
import pandas as pd


class ABM:
    @staticmethod
    def agregarUsuario(nombre, contrasena, cuil, telef, x, y):
        a = M_Anses.Anses("ciudadano").confirmarCuil(cuil)
        b = M_Anses.Anses("ciudadano").confirmarTelef(telef)
        c = M_Anses.Anses("ciudadano").confirmarNombre(nombre)
        if a or b or c:
            return print("Datos ya usados, intentelo de nuevo")
        else:
            f = open("../Database/DB_ciudadano.csv", "a", newline="")
            writer = csv.writer(f)
            tupla_nueva = (nombre, contrasena, cuil, telef, x, y, "n", 0)
            writer.writerow(tupla_nueva)

    @staticmethod
    def getBlock(tipo_usuario, tipo_ingreso, ingreso):
        df = pd.read_csv(f"../Database/DB_{tipo_usuario}.csv")
        df.head(6)
        # Busco el nombre y cambio el cvs a bloqueado
        df.set_index(tipo_ingreso, inplace=True)
        a = df.loc[ingreso]['Bloqueado'] == "y"
        return a
