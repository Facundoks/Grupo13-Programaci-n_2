from Usuario.U_Usuario import Usuario
from Monitoreo.M_Solicitudes import Solicitud

import pandas as pd


class Ciudadano(Usuario):
    def __init__(self, cuil, telef, contra):
        self.cuil = cuil
        self.telef = telef
        self.contra = contra
        self.amigos = []
        self.solicitudes = []
        self.rechazadas = 0
        self.ingresarCiudadano("Cuil", self.cuil, self.contra)

    def getCuil(self):
        return self.cuil

    def enviarSolicitud(self, receptor):
        solicitud = Solicitud(self, receptor)
        solicitud.enviar(self.cuil)

    def recibirSolicitud(self, solicitud):
        self.solicitudes.append(solicitud)

    def aceptarSolictud(self, num):
        self.amigos.append(self.solicitudes[num])
        del self.solicitudes[num]

    def rechazarSolicitud(self, num, emisor):
        rechazo = Solicitud(self, emisor)
        rechazo.conteo_rechazoSolicitud()
        del self.solicitudes[num]

    def getSolicitud(self):
        return self.solicitudes

    def getRechazadas(self):
        return self.rechazadas

    def getAmigos(self):
        return self.amigos

    def reportarEvento(self, evento):
        evento.participantes.append(self)
        self.reportarEvento_csv(evento)

    def reportarEvento_csv(self, evento):
        tipo_evento = evento.getTipo()
        df = pd.read_csv("../Database/DB_evento.csv")
        df.loc[df["Tipo"] == tipo_evento, "Participantes"] += 1
        df.to_csv("../Database/DB_evento.csv", index=False)

    def vincular_evento(self, evento, list_ciudadanos):
        self.ingresarCiudadano("Cuil", self.cuil, self.contra)
        for ciudadano in list_ciudadanos:
            evento.participantes.append(ciudadano)
        evento.participantes.append(self)
        self.vincular_evento_csv(evento)

    def vincular_evento_csv(self, evento):
        tipo_evento = evento.getTipo()
        part_evento = len(evento.getParticipantes())
        df = pd.read_csv("../Database/DB_evento.csv")
        df.loc[df["Tipo"] == tipo_evento, "Participantes"] = part_evento
        df.to_csv("../Database/DB_evento.csv", index=False)


