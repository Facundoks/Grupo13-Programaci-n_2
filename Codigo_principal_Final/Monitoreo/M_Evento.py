import pandas as pd
from Usuario.U_Administrador import Admin

class Evento:
    def __init__(self, tipo, coordenada_x, coordenada_y):
        self.tipo = tipo
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.estado = "Baja"
        self.participantes = []

    def indCalor(self):
        self.estado = "Alta"
        Admin(99999999999, 3777392328, "patas").darAlta(self.tipo)
        a = self.getParticipantes_csv()
        x = int(self.coordenada_x)
        y = int(self.coordenada_y)
        df = pd.read_csv("../Database/DB_mapa2.csv")
        df.head(8)
        df = pd.read_csv("../Database/DB_mapa2.csv")
        df.iloc[y-1][x] += a
        df.to_csv("../Database/DB_mapa2.csv", index=False)

    def getParticipantes_csv(self):
        df = pd.read_csv(f"../Database/DB_evento.csv")
        df.set_index("Tipo", inplace=True)
        a = df.loc[self.tipo]['Participantes']
        return a

    def getParticipantes(self):
        return self.participantes

    def getNumParticipantes(self):
        return len(self.participantes)

    def getTipo(self):
        return self.tipo

