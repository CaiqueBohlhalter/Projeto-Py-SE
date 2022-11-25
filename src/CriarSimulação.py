from Simulador import Simulador
from MathResources.StandardDeviation import StandardDeviaton
from MathResources.Average import Average
import math

class CriarSimulação:
  def __init__(self) -> None:
    self.clientesSimulados = [100, 50, 75, 99, 77, 30, 40]
    self.QTD_SIMULAÇÕES = self.clientesSimulados.__len__()

    self.mediaEsperaFila = []
    self.mediaTempoServiço = []
    self.mediaTempoNoSistema = []

    self.mediaFilaTotal = Average()
    self.mediaServiçoTotal = Average()
    self.mediaSistemaTotal = Average()

    self.desvioFila = StandardDeviaton()
    self.desvioServiço = StandardDeviaton()
    self.desvioSistema = StandardDeviaton()

    self.intervaloFila = 0
    self.intervaloServiço = 0
    self.intervaloSistema = 0

  def iniciarSimulação(self):
    simulando = Simulador()

    # Escolhe imprimir todos valores ou não
    simulando.setPrintTempos(False)
    simulando.setPrintMedias(False)

    for i in range(self.QTD_SIMULAÇÕES):
      simulando.setQuantidadeClientes(self.clientesSimulados[i])
      simulando.simular()
      self.mediaEsperaFila.append(simulando.getMediaEsperaFila().average) 
      self.mediaTempoServiço.append(simulando.getMediaTempoServiço().average)
      self.mediaTempoNoSistema.append(simulando.getMediaTempoNoSistema().average)

    self.calculaDesvioPadrao()
    self.calculaIntervaloDeConfiança()

    print(f"Média Tempo de fila: {self.mediaFilaTotal.getValue()}s")
    print(f"Tempo de fila Max: {self.mediaFilaTotal.getValue() + self.intervaloFila} // Tempo de fila Min: {self.mediaFilaTotal.getValue() - self.intervaloFila}")

    print(f"\nMédia Tempo de Serviço: {self.mediaServiçoTotal.getValue()}s")
    print(f"Tempo de Serviço Max: {self.mediaServiçoTotal.getValue() + self.intervaloServiço} // Tempo de Serviço Min: {self.mediaServiçoTotal.getValue() - self.intervaloServiço}")

    print(f"\nMédia Tempo no Sistema: {self.mediaSistemaTotal.getValue()}s")
    print(f"Tempo Sistema Max: {self.mediaSistemaTotal.getValue() + self.intervaloSistema} // Tempo Sistema Min: {self.mediaSistemaTotal.getValue() - self.intervaloSistema}")


  def calculaDesvioPadrao(self):
    
    # Retira médias das amostragens de medias nas simulações
    self.mediaFilaTotal.setTimes(self.QTD_SIMULAÇÕES)
    self.mediaFilaTotal.calculate(self.mediaEsperaFila)
    
    self.mediaServiçoTotal.setTimes(self.QTD_SIMULAÇÕES)
    self.mediaServiçoTotal.calculate(self.mediaTempoServiço)

    self.mediaSistemaTotal.setTimes(self.QTD_SIMULAÇÕES)
    self.mediaSistemaTotal.calculate(self.mediaTempoNoSistema)

    # Obtem desvio padrão desses valores
    self.desvioFila.setTimes(self.QTD_SIMULAÇÕES)
    self.desvioFila.calculate(self.mediaEsperaFila, self.mediaFilaTotal.getValue())
    self.desvioServiço.setTimes(self.QTD_SIMULAÇÕES)
    self.desvioServiço.calculate(self.mediaTempoServiço, self.mediaServiçoTotal.getValue())
    self.desvioSistema.setTimes(self.QTD_SIMULAÇÕES)
    self.desvioSistema.calculate(self.mediaTempoNoSistema, self.mediaSistemaTotal.getValue())
  
  def calculaIntervaloDeConfiança(self):
    omegaFila = self.desvioFila.getValue() / (math.sqrt(self.QTD_SIMULAÇÕES))
    self.intervaloFila = omegaFila * 1.96

    omegaServiço = self.desvioServiço.getValue() / (math.sqrt(self.QTD_SIMULAÇÕES))
    self.intervaloServiço = omegaServiço * 1.96

    omegaSistema = self.desvioSistema.getValue() / (math.sqrt(self.QTD_SIMULAÇÕES))
    self.intervaloSistema = omegaSistema * 1.96


if __name__ == '__main__':
  simulação = CriarSimulação()
  simulação.iniciarSimulação()
