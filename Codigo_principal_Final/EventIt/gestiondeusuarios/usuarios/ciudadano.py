from gestiondeeventos.contactos import Contactos
from gestiondeeventos.evento import Evento
from gestiondeusuarios.atributosUsuarios.telefono import Telefono
from gestiondeusuarios.atributosUsuarios.cuil import Cuil
from gestiondeusuarios.atributosUsuarios.password import Password

class Ciudadano:
    def __init__(self, telefono, cuil, password):
        self.telefono = Telefono(telefono)
        self.cuil = Cuil(cuil)
        self.password = Password(password)
        self.estado=True
        self.rechazos=0
        self.contactos = Contactos()
        self.eventos=[]

    def getCuil(self):
        return str(self.cuil)

    def getTelefono(self):
        return self.telefono

    def getContrasena(self):
        return str(self.password)

    def setEstado(self,estado:bool):
        self.estado = estado

    def getstate(self):
        return self.estado

    def Enviarinvitacion(self,contacto):
        contacto.contactos.setRecibidas(self)
        self.contactos.setEnviadas(contacto)

    def rechazarInvitacion(self,ciudadano):
        """Se fija en la lista de invitaciones si esta la invitacion y si no esta salta error"""
        if (ciudadano in self.contactos.getRecibidas()) and (self in ciudadano.contactos.getEnviadas()):
            self.contactos.removeEnviadas(ciudadano)
            ciudadano.contactos.removeRecibidas(self)
            ciudadano.setRechazo()
        else:
            raise ValueError("Este ciudadano no te ha enviado una solicitud")

    def aceptarInvitacion(self,ciudadano):
        if (ciudadano in self.contactos.getRecibidas()) and (self in ciudadano.contactos.getEnviadas()):
            self.contactos.getRecibidas().remove(ciudadano)
            ciudadano.contactos.getEnviadas().remove(self)
            self.contactos.getAmigos().append(ciudadano)
            ciudadano.contactos.getAmigos().append(self)
        else:
            raise ValueError("Este ciudadano no te ha enviado una solicitud")

    def asistirEvento(self,tipo,x,y):
        """Crear evento,appendearlo en un lugar que sea eventos activos"""
        self.eventos.append(Evento(tipo,x,y))

    def getEventos(self):
        return self.eventos

    def setRechazo(self):
        self.rechazos +=1


