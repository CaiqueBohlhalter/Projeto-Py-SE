class Fila():
    
    def __init__(self) -> None:
      self.empty = True
      self.tempoServiçoTotal = 0
      self.ts = []
      self.tec = []
      self.espera = []
      self.clientes = 0
      self.tempoFinalServiço = 0
      self.mediaTs = 0
      self.mediaEspera = 0
      self.mediaSistema = 0
        
    def adicionarServiço(self, ts, espera):
        self.ts.append(ts)
        self.espera.append(espera)
        self.clientes += 1
        self.tempoFinalServiço += ts + espera

    def calcularMedias(self):
        self.calcularMediaTempoServiço()

        self.calcularMediaTempoEspera()

        self.calcularMediaTempoNoSistema()

    def calcularMediaTempoServiço(self):
        sum = 0
        for i in range(len(self.ts)):
            sum += self.ts[i]

        self.mediaTs = sum / self.clientes

    def calcularMediaTempoEspera(self):
        sum = 0
        for i in range(len(self.espera)):
            sum = sum + self.espera[i]

        self.mediaEspera = sum / self.clientes 

    def calcularMediaTempoNoSistema(self):
        self.mediaSistema = self.tempoFinalServiço / self.clientes 

    def setTEC(self, tec):
        self.tec.append(tec)

    def getStatus(self):
        return self.empty

    def getTsTotal(self):
        sum = 0
        for i in range(0, len(self.tec)):    
            sum = sum + self.tec[i]; 

        for i in range(0, len(self.ts)):    
            sum = sum + self.ts[i]; 

        return sum

    def getTempoFinalServiço(self):
        return self.tempoFinalServiço

    def getMediaSistema(self):
        return self.mediaSistema / 60
    
    def getMediaEspera(self):
        return self.mediaEspera / 60
    
    def getMediaTempoServiço(self):
        return self.mediaTs