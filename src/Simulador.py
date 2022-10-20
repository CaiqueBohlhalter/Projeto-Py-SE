#!/usr/bin/env python

from Gerador import Gerador
from MathResources.Tec import Tec
from MathResources.Ts import Ts
from ImprimirDados import ImprimirDados

# -- Constantes
QUANTIDADE_DE_CLIENTES = 5
CONST_A = 15
CONST_B = 35

# -- Valores a serem obtidos
tempoChegada = []
tempoInicioServiço = []
tempoFimServiço = []
tempoFila = []
tempoNoSistema = []
tempoLivre = []

imprimir = ImprimirDados()

# -- Gerador de valores aleatórios orientado a quantidade
def gerador():
  gerador = Gerador()
  gerador.setSize(QUANTIDADE_DE_CLIENTES * 2)
  gerador.generate()
  generated_values = gerador.getGeneratedValues()
  return generated_values

# -- Gerador de valores de tempo entre clientes
def geradorTec(values):
  tec = Tec()
  return tec.calculate(values)

# -- Gerador de valores de tempo de serviço
def geradorTs(values, a, b):
  ts = Ts()
  return ts.calculate(values, a, b)

# -- Define Inicio e término de cada serviço para cada cliente
def calculaTempoServiço():
  # --  Define estáticamente os valores do primeiro cliente
  tempoInicioServiço.append(tempoChegada[0])
  tempoFimServiço.append(tempoInicioServiço[0] + tsArray[0])

  # --  Define dinamicamente os valores dos demais clientes
  for i in range(1, QUANTIDADE_DE_CLIENTES):
    tempoInicioServiço.append(tempoFimServiço[i-1])
    tempoFimServiço.append(tempoInicioServiço[i] + tsArray[i])

# -- Calcula os tempos de chegada dos clientes
def calculaTempoChegada():
  # -- Atribui ao primeiro cliente o primeiro momento com cliente
  tempoChegada.append(tecArray[0])

  for i in range(1, QUANTIDADE_DE_CLIENTES):
    tempoChegada.append(tempoChegada[i-1] + tecArray[i]) 

# -- Calcula o tempo que cada cliente esperou na fila
def calculaTempoNaFila():
  # -- Primeiro cliente não pegou fila
  tempoFila.append(0)

  for i in range(1, QUANTIDADE_DE_CLIENTES):
    tempoFila.append(tempoInicioServiço[i] - tempoChegada[i])

# -- Calcula o tempo que cada cliente passou dentro do estabelecimento
def calculaTempoNoSistema():
  for i in range(QUANTIDADE_DE_CLIENTES):
    tempoNoSistema.append(tempoFila[i] + tsArray[i])

# -- Calcula o tempo que o sistema esteve livre
def calculaTempoLivre():
  # -- Tempo livre até o primeiro cliente chegar
  tempoLivre.append(tecArray[0])

  for i in range(1, QUANTIDADE_DE_CLIENTES):
    if(tempoFila[i] == 0):
      tempoLivre.append(tempoInicioServiço[i] - tempoFimServiço[i-1])
    else:
      tempoLivre.append(0)

# -- Obtem valores dos tempos analisados
def calculaTempos():
  calculaTempoChegada()
  calculaTempoServiço()
  calculaTempoNaFila()
  calculaTempoNoSistema()
  calculaTempoLivre()


##--------------------MAIN--------------------##

# -- Obtem Valores Aleatorios
values = gerador()

# -- Obtem Tec e Ts baseado nos valores aleatórios
tecArray = geradorTec(values)
tsArray = geradorTs(values, CONST_A, CONST_B)

calculaTempos()

imprimir.printTempos(tecArray, tsArray, tempoChegada, tempoInicioServiço, tempoFimServiço, tempoFila, tempoNoSistema, tempoLivre, QUANTIDADE_DE_CLIENTES)
 
