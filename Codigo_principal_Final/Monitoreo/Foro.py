class Registro_evento:
    def __init__(self):
        self.reportedEventos = []

    def appendEvent(self, evento):
        self.reportedEventos.append(evento)
        return self.reportedEventos

    def getReported(self):
        return self.reportedEventos
