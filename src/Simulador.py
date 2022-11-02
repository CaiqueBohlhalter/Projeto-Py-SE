#!/usr/bin/env python

from Gerador import Gerador
from MathResources.Tec import Tec
from MathResources.Ts import Ts
from ImprimirDados import ImprimirDados
from MathResources.Average import Average

class Simulador:

  def __init__(self) -> None:
    # -- Constantes
    self.QUANTIDADE_DE_CLIENTES = 11
    self.CONST_A = 15
    self.CONST_B = 35

    # -- Valores a serem obtidos
    self.tempoChegada = []
    self.tempoInicioServiço = []
    self.tempoFimServiço = []
    self.tempoFila = []
    self.tempoNoSistema = []
    self.tempoLivre = []

    self.mediaEsperaFila = Average()
    self.mediaTempoServiço = Average()
    self.mediaTempoNoSistema = Average()

    self.imprimir = ImprimirDados()

    self.tecArray = []
    self.tsArray = []

  def simular(self):
    # -- Obtem Valores Aleatorios
    values = self.gerador()

    # -- Obtem Tec e Ts baseado nos valores aleatórios
    self.tecArray = self.geradorTec(values)
    self.tsArray = self.geradorTs(values, self.CONST_A, self.CONST_B)

    self.calculaTempos()
    self.imprimir.printTempos(self.tecArray, self.tsArray, self.tempoChegada, self.tempoInicioServiço, 
      self.tempoFimServiço, self.tempoFila, self.tempoNoSistema, self.tempoLivre, self.QUANTIDADE_DE_CLIENTES)

    self.calculaMedias()
    self.imprimir.printMedias(self.mediaEsperaFila.getValue(), self.mediaTempoServiço.getValue(), 
      self.mediaTempoNoSistema.getValue(), self.calculaProbabilidadeCaixaLivre())

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

  # -- Define Inicio e término de cada serviço para cada cliente
  def calculaTempoServiço(self):
    # --  Define estáticamente os valores do primeiro cliente
    self.tempoInicioServiço.append(self.tempoChegada[0])
    self.tempoFimServiço.append(self.tempoInicioServiço[0] + self.tsArray[0])

    # --  Define dinamicamente os valores dos demais clientes
    for i in range(1, self.QUANTIDADE_DE_CLIENTES):
      self.tempoInicioServiço.append(self.tempoFimServiço[i-1])
      self.tempoFimServiço.append(self.tempoInicioServiço[i] + self.tsArray[i])

  # -- Calcula os tempos de chegada dos clientes
  def calculaTempoChegada(self):
    # -- Atribui ao primeiro cliente o primeiro momento com cliente
    self.tempoChegada.append(self.tecArray[0])

    for i in range(1, self.QUANTIDADE_DE_CLIENTES):
      self.tempoChegada.append(self.tempoChegada[i-1] + self.tecArray[i]) 

  # -- Calcula o tempo que cada cliente esperou na fila
  def calculaTempoNaFila(self):
    # -- Primeiro cliente não pegou fila
    self.tempoFila.append(0)

    for i in range(1, self.QUANTIDADE_DE_CLIENTES):
      self.tempoFila.append(self.tempoInicioServiço[i] - self.tempoChegada[i])

  # -- Calcula o tempo que cada cliente passou dentro do estabelecimento
  def calculaTempoNoSistema(self):
    for i in range(self.QUANTIDADE_DE_CLIENTES):
      self.tempoNoSistema.append(self.tempoFila[i] + self.tsArray[i])

  # -- Calcula o tempo que o sistema esteve livre
  def calculaTempoLivre(self):
    # -- Tempo livre até o primeiro cliente chegar
    self.tempoLivre.append(self.tecArray[0])

    for i in range(1, self.QUANTIDADE_DE_CLIENTES):
      if(self.tempoFila[i] == 0):
        self.tempoLivre.append(self.tempoInicioServiço[i] - self.tempoFimServiço[i-1])
      else:
        self.tempoLivre.append(0)

  # -- Obtem valores dos tempos analisados
  def calculaTempos(self):
    self.calculaTempoChegada()
    self.calculaTempoServiço()
    self.calculaTempoNaFila()
    self.calculaTempoNoSistema()
    self.calculaTempoLivre()

  # -- Obtem valores das médias
  def calculaMedias(self):
    self.mediaEsperaFila.setTimes(self.QUANTIDADE_DE_CLIENTES)
    self.mediaTempoServiço.setTimes(self.QUANTIDADE_DE_CLIENTES)
    self.mediaTempoNoSistema.setTimes(self.QUANTIDADE_DE_CLIENTES)
    
    self.mediaEsperaFila.calculate(self.tempoFila)
    self.mediaTempoServiço.calculate(self.tsArray)
    self.mediaTempoNoSistema.calculate(self.tempoNoSistema)

  # -- Obtem a probabilidade do caixa estar livre
  def calculaProbabilidadeCaixaLivre(self):
    somaTempoLivre = sum(self.tempoLivre)
    return somaTempoLivre/self.tempoFimServiço[self.QUANTIDADE_DE_CLIENTES - 1] 

  # -- Determina quantidade de clientes da simulação
  def setQuantidadeClientes(self, clientes):
    self.QUANTIDADE_DE_CLIENTES = clientes

  # -- Retornar Médias calculadas na simulação
  def getMediaEsperaFila(self):
    return self.mediaEsperaFila

  def getMediaTempoServiço(self):
    return self.mediaTempoServiço

  def getMediaTempoNoSistema(self):
    return self.mediaTempoNoSistema




