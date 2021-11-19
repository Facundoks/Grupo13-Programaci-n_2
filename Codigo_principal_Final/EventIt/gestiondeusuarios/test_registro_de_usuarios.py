from gestiondeeventos.sensor import Sensor
from registrodeciudadano import GestiondeUsuarios
from usuarios.ciudadano import Ciudadano

Eventit=GestiondeUsuarios()
Eventit.registro(27442321022,543416526366,"micontraseña")
Eventit.registro(20430042947,54902975162742,"micontraseña")
Eventit.registro(20230326992,5402975071881,"micontraseña")
print(Eventit.getCiudadanos())

fran = Eventit.logCiudadano(27442321022,"micontraseña")
juli = Eventit.logCiudadano(20430042947,"micontraseña")
taty = Eventit.logCiudadano(20230326992,"micontraseña")

print(fran)
fran.asistirEvento("Deportivo",1,2)
fran.asistirEvento("Vacunacion",1,3)
fran.asistirEvento("espectaculo",1,1)
print(juli)
juli.asistirEvento("Vacunacion",1,3)
juli.asistirEvento("Deportivo",1,2)
print(taty)
taty.asistirEvento("Deportivo",1,2)
#Zona1= Sensor(1,2)
#Zona1.filtrarEventos(Eventit.getCiudadanos())
#Zona2 = Sensor(1,3)
#Zona2.filtrarEventos(Eventit.getCiudadanos())

fran.Enviarinvitacion(Eventit.buscarusuario(20430042947))
print(fran.contactos.getEnviadas())
juli.aceptarInvitacion(Eventit.buscarusuario(27442321022))
print(juli.contactos.getAmigos())
fran.Enviarinvitacion(Eventit.buscarusuario(20230326992))

taty.rechazarInvitacion(27442321022)



