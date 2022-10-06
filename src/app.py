#!/usr/bin/env python

from Gerador import Gerador
from MathResources.Average import Average
from MathResources.StandardDeviation import StandardDeviaton
from MathResources.Covariance import Covariance
from MathResources.QuiSquare import QuiSquare
from Gerador import Gerador
from GeradorCongLinear import GeradorCongLinear

SIZE_OF_ARRAY = 8000

# -- instantiate calculators
average = Average()
standard_deviaton = StandardDeviaton()
covariance = Covariance()
quiSquare = QuiSquare()

def printAllValues():
  average.printResult()
  standard_deviaton.printResult()
  covariance.printResult()
  quiSquare.printResult()

def gerador():
  # -- generate seed values
  gerador = Gerador()
  gerador.setSize(SIZE_OF_ARRAY)
  gerador.generate()
  generated_values = gerador.getGeneratedValues()
  return generated_values

def callLinearGenerator():
  # -- generate seed values
  gerador = GeradorCongLinear()
  gerador.setSize(SIZE_OF_ARRAY)
  gerador.setMod(1024)
  gerador.generate(16807, 192)
  
  generated_values = gerador.getGeneratedValues()
  return generated_values

values = gerador()

# -- calulate and print results
average.setTimes(SIZE_OF_ARRAY)
average.calculate(values)

standard_deviaton.setTimes(SIZE_OF_ARRAY)
standard_deviaton.calculate(values, average.getValue())

covariance.setTimes(SIZE_OF_ARRAY)
covariance.calculate(values)

quiSquare.setTimes(SIZE_OF_ARRAY)
quiSquare.calculate(values)

printAllValues()
