from SimuladorDiversasFilas import Simulador
from MathResources.StandardDeviation import StandardDeviaton
from MathResources.Average import Average

class CriarSimulação:
  def __init__(self) -> None:
    self.clientesSimulados = [90]
    self.QTD_SIMULAÇÕES = self.clientesSimulados.__len__()
    self.tsManual = [5,7,5,20,25,15,2]
    self.tecManual = [1,2,3,6,5,2,3]
    self.usarArrayTeste = True

  def iniciarSimulação(self):
    simulando = Simulador()

    if(self.usarArrayTeste):
      simulando.setQuantidadeClientes(len(self.tsManual))
      simulando.setModoTesteManual(self.tsManual, self.tecManual)
      simulando.simular()

    else:
      for i in range(self.QTD_SIMULAÇÕES):
        simulando.setQuantidadeClientes(self.clientesSimulados[i])
        simulando.simular()

if __name__ == '__main__':
  simulação = CriarSimulação()
  simulação.iniciarSimulação()
