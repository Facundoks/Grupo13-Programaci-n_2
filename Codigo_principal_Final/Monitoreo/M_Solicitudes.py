import pandas as pd


class Solicitud:
    def __init__(self, emisor, receptor):
        self.emisor = emisor
        self.receptor = receptor

    def enviar(self, cuil):
        self.receptor.recibirSolicitud(cuil)
#       self.receptor.solicitud_pendiente(self)

    def conteo_rechazoSolicitud(self):
        self.receptor.rechazadas += 1
        Solicitud(self.emisor, self.receptor).conteo_rechazoSolicitud_csv()
        Solicitud(self.emisor, self.receptor).rechazoBloqueo()

    def conteo_rechazoSolicitud_csv(self):
        cuil = self.receptor.getCuil()
        df = pd.read_csv("../Database/DB_ciudadano.csv")
        df.loc[df["Cuil"] == cuil, "Rechazada"] += 1
        df.to_csv("../Database/DB_ciudadano.csv", index=False)

    def rechazoBloqueo(self):
        cuil = self.receptor.getCuil()
        df = pd.read_csv(f"../Database/DB_ciudadano.csv")
        df.set_index("Cuil", inplace=True)
        a = df.loc[cuil]['Rechazada'] >= 5
        if a:
            df = pd.read_csv("../Database/DB_ciudadano.csv")
            df.loc[df["Cuil"] == cuil, "Bloqueado"] = "y"
            df.to_csv("../Database/DB_ciudadano.csv", index=False)

    def __repr__(self):
        return f'Usted tiene una solicitud de amistad de {self.emisor.get_nombre()}'
