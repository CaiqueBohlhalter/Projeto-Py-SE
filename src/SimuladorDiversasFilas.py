#!/usr/bin/env python

from ValueGenerators.Gerador import Gerador
from MathResources.Tec import Tec
from MathResources.Ts import Ts
from Fila import Fila

class Simulador:

  def __init__(self) -> None:
    # -- Constantes
    self.QUANTIDADE_DE_CLIENTES = 11
    self.QUANTIDADE_DE_FILAS = 2
    self.CONST_A = 15
    self.CONST_B = 35

    self.isManual = False

    self.tecArray = []
    self.tsArray = []

    #Filas
    self.fila1 = Fila()
    self.fila2 = Fila()
    self.tempoSimulado = 0
    self.tempoChegada = 0

  def simular(self):
    if not self.isManual:  
      # -- Obtem Valores Aleatorios
      values = self.gerador()

      # -- Obtem Tec e Ts baseado nos valores aleatórios
      self.tecArray = self.geradorTec(values)
      self.tsArray = self.geradorTs(values, self.CONST_A, self.CONST_B)

    self.simularFilas(self.tecArray, self.tsArray)

  def simularFilas(self, tec, ts):
    tempoFinal = 0

    for i in range(0, self.QUANTIDADE_DE_CLIENTES):
      if self.tempoSimulado > tempoFinal:
        tempoFinal = self.tempoSimulado

      if i > 0:
        self.tempoChegada += tec[i]

        if(self.fila1.getTempoFinalServiço() <= self.fila2.getTempoFinalServiço()):
          self.adicionarClienteFila(self.fila1, tec, ts, i)
        else:
          self.adicionarClienteFila(self.fila2, tec, ts, i)

      else:
        self.tempoSimulado = ts[i]
        self.adicionarClienteFila(self.fila1, tec, ts, i)
  

    self.fila1.calcularMedias()
    self.fila2.calcularMedias()

    print(f"--------------------------------------------")
    print(f"TEMPO TOTAL SIMULADO: {tempoFinal}s")
    print(f"--------------------------------------------")

    self.imprimirDadosFila(self.fila1, 1)
    self.imprimirDadosFila(self.fila2, 2)


  def imprimirDadosFila(self ,fila, num):
    print(f"\nFila {num}------->\nTempo Médio de Serviço: {round(fila.getMediaTempoServiço())} s")
    print(f"\nTempo Médio de Espera na Fila: {fila.getMediaEspera()} min")
    print(f"\nTempo Médio Gasto no Sistema: {fila.getMediaSistema()} min")

  def adicionarClienteFila(self, filaAtual, tec, ts, i):
    if(self.tempoChegada >= filaAtual.getTempoFinalServiço()):
      tempoEspera = self.tempoChegada - filaAtual.getTempoFinalServiço()

      self.tempoSimulado = (self.tempoSimulado - ts[i-1]) + tec[i] + ts[i]
      filaAtual.adicionarServiço(ts[i], tempoEspera)

    else:
      tempoEntreClientes = filaAtual.getTempoFinalServiço() - self.tempoChegada
      
      filaAtual.setTEC(tempoEntreClientes)
      filaAtual.adicionarServiço(ts[i], tempoEntreClientes)

      self.tempoSimulado += tec[i] + ts[i]

  # -- Gerador de valores aleatórios orientado a quantidade
  def gerador(self):
    gerador = Gerador()
    gerador.setSize(self.QUANTIDADE_DE_CLIENTES * 2)
    gerador.generate()
    generated_values = gerador.getGeneratedValues()
    return generated_values

  # -- Gerador de valores de tempo entre clientes
  def geradorTec(self, values):
    tec = Tec()
    return tec.calculate(values)

  # -- Gerador de valores de tempo de serviço
  def geradorTs(self, values, a, b):
    ts = Ts()
    return ts.calculate(values, a, b)

  # -- Determina quantidade de clientes da simulação
  def setQuantidadeClientes(self, clientes):
    self.QUANTIDADE_DE_CLIENTES = clientes

  # -- Escolhe usar valores escolhidos ao invés dos gerados  
  def setModoTesteManual(self, ts, tec):
    self.isManual = True
    self.tsArray = ts
    self.tecArray = tec
  