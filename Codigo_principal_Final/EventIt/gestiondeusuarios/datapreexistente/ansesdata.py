import csv
import pandas as pd

class AnsesData:
    __cuil=[]
    __telefono=[]

    @classmethod
    def compararCuilyTelefono(cls, cuil, telefono):
        AnsesData.deColumnaaLista()
        if cls.__cuil.index(cuil) == cls.__telefono.index(telefono):
            return True
        else:
            raise ValueError("Cuil o telefono incorrecto")


    @classmethod
    def deColumnaaLista(cls):
        with open(r"C:\Users\Francisco\Desktop\Prog 2\EventIt\gestiondeusuarios\datapreexistente\anses.csv","r+") as archivo:
            header = next(archivo)
            column_names=["cuil","telefono"]
            df = pd.read_csv(archivo,names=column_names)
            cls.__cuil=df.cuil.tolist()
            cls.__telefono =df.telefono.tolist()

    @classmethod
    def getList(cls):
        return cls.__cuil
