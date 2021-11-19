from abm import ABM

#Registrar un administrador

#ABM.habilitarAdministrador("francisco","contraseña")
#ABM.habilitarAdministrador("vicky","contraseña")

fran = ABM.iniciarAdministrador("francisco", "contraseña")
fran.crearEvento("Deporte",2,1)

