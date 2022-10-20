class ImprimirDados():
    
    def __init__(self) -> None:
      self.times = 10

    def printTempos(self, tec, ts, tempoChegada, tempoInicioServiço, tempoFimServiço, tempoFila, tempoSistema, tempoLivre, times):
      self.times = times
      for i in range(self.times):
        print(f"-----------------------------{i+1}----------------------------------------")
        self.printTec(tec, i)
        self.printTs(ts, i)
        self.printTempoChegada(tempoChegada, i)
        self.printInicioServiço(tempoInicioServiço, i)
        self.printFimServiço(tempoFimServiço, i)
        self.printTempoFila(tempoFila, i)
        self.printTempoNoSistema(tempoSistema, i)
        self.printTempoLivre(tempoLivre, i)


    def printTec(self, tec, i):
      print(f"TEC: {tec[i]} " )

    def printTs(self, ts, i):
      print(f"TS: {ts[i]} " )

    def printTempoChegada(self, tempoChegada, i):
      print(f"TCH: {tempoChegada[i]} " )

    def printInicioServiço(self, tempoInicioServiço, i):
      print(f"TIS: {tempoInicioServiço[i]} " )

    def printFimServiço(self, tempoFimServiço, i):
      print(f"TFS: {tempoFimServiço[i]} " )

    def printTempoFila(self, tempoFila, i):
      print(f"TFL: {tempoFila[i]} " )

    def printTempoNoSistema(self, tempoSistema, i):
      print(f"TNS: {tempoSistema[i]} " )

    def printTempoLivre(self, tempoLivre, i):
      print(f"TLV: {tempoLivre[i]} " ) 

    
    

    

