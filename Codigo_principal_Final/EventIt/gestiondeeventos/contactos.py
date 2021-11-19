class Contactos:
    def __init__(self):
        """Solicitudes recibidas y invitaciones enviadas"""
        self.enviadas = []
        self.recibidas = []
        self.bff = []

    def leerSolicitudes(self):
        pass

    def leerinvitaciones(self):
        pass

    def getEnviadas(self):
        return self.enviadas

    def getRecibidas(self):
        return self.recibidas

    def getAmigos(self):
        return self.bff

    def setRecibidas(self,contacto):
        self.recibidas.append(contacto)

    def setEnviadas(self,contacto):
        self.enviadas.append((contacto))

    def removeEnviadas(self,contactos):
        self.enviadas.remove(contactos)

    def removeRecibidas(self,contacto):
        self.recibidas.remove(contacto)

