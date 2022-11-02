
from Simulador import Simulador


class CriarSimulação:
  def __init__(self) -> None:
    self.clientesSimulados = [100, 50, 75, 99]

    self.mediaEsperaFila = []
    self.mediaTempoServiço = []
    self.mediaTempoNoSistema = []

  def iniciarSimulação(self):
    simulando = Simulador()

    simulando.setQuantidadeClientes(self.clientesSimulados[0])
    simulando.simular()

if __name__ == '__main__':
  simulação = CriarSimulação()
  simulação.iniciarSimulação()
