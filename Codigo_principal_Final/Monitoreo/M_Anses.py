import csv
import pandas as pd


class Anses:
    # Diferenciamos si es ciudadano o admin con la variable tipo
    def __init__(self, tipo):
        self.tipo = tipo

    def confirmacion(self, dato, num):
        tipo = self.tipo.lower()
        with open(f"../Database/DB_{tipo}.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            for linea in reader:
                if dato == linea[num]:
                    return True
            return False

    def confirmarNombre(self, nombre):
        return Anses(self.tipo).confirmacion(nombre, 0)

    def confirmarContra(self, tipo_ingreso, ingreso, contra):
        ciu = self.tipo.lower()
        df = pd.read_csv(f"../Database/DB_{ciu}.csv")
        df.set_index(tipo_ingreso, inplace=True)
        a = df.loc[ingreso]['Contrasena'] == contra
        return a

    @staticmethod
    def confirmarCuil(dato):
        with open(f"../Database/DB_anses.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            for linea in reader:
                if dato == linea[0]:
                    return True
            return False

    @staticmethod
    def agregarCuil(dato):
        f = open("../Database/DB_anses.csv", "a", newline="")
        writer = csv.writer(f)
        writer.writerow([dato])

    def confirmarTelef(self, telef):
        return Anses(self.tipo).confirmacion(telef, 3)

    def confirmarZonax(self, x):
        return Anses(self.tipo).confirmacion(x, 4)

    def confirmarZonay(self, y):
        return Anses(self.tipo).confirmacion(y, 5)

