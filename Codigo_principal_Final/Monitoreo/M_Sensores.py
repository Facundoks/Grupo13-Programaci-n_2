from Monitoreo.M_Evento import Evento
import csv
import pandas as pd


class Sensores:
    @staticmethod
    def generarEvento(tipo, x, y):
        evento_instanciado = Evento(tipo, x, y)
        Sensores.generarEvento_csv(tipo, x, y)
        return evento_instanciado

    @staticmethod
    def reportarEvento(tipo, num):
        df = pd.read_csv("../Database/DB_evento.csv")
        df.loc[df["Tipo"] == tipo, "Participantes"] += num
        df.to_csv("../Database/DB_evento.csv", index=False)

    @staticmethod
    def generarEvento_csv(tipo, x, y):
        f = open("../Database/DB_evento.csv", "a", newline="")
        writer = csv.writer(f)
        tupla_nueva = (tipo, x, y, "Baja", 0)
        writer.writerow(tupla_nueva)

