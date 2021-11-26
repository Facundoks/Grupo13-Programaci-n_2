import pandas as pd
from Monitoreo.Manipulacion_csv import writelist, getValue


class Solicitud:
    def __init__(self, transmitter, receiver):
        self.transmitter = transmitter
        self.receiver = receiver

    #En caso que se envie una solicitud
    def send(self, friend_request):
        name = self.receiver.name
        writelist("DB_Csolicitudes", 'Name', 'Friend_request', name, friend_request, ['Nada que encontrar...'])

#   En caso que se rechace la solicitud
    def sumRejected_requests(self):
        self.receiver.rejected_requests += 1
        Solicitud(self.transmitter, self.receiver).sumRejected_requests_csv()
        Solicitud(self.transmitter, self.receiver).rejectedBlocking_cvs()

    def sumRejected_requests_csv(self):
        name = self.receiver.getname()
        df = pd.read_csv("../Database/DB_ciudadano.csv")
        df.loc[df["Name"] == name, "Rejected_requests"] += 1
        df.to_csv("../Database/DB_ciudadano.csv", index=False)

    def rejectedBlocking_cvs(self):
        name = self.receiver.getname()
        rejected = getValue('DB_ciudadano', 'Name', 'Rejected_requests', name)
        if rejected >= 5:
            df = pd.read_csv("../Database/DB_ciudadano.csv")
            df.loc[df["Name"] == name, "Blocked"] = "y"
            df.to_csv("../Database/DB_ciudadano.csv", index=False)
