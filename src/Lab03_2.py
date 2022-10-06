#!/usr/bin/env python

from turtle import color
import matplotlib.pyplot as plotter
from MathResources.Average import Average
from MathResources.StandardDeviation import StandardDeviaton
from MathResources.Covariance import Covariance
from MathResources.QuiSquare import QuiSquare
from Gerador import Gerador
from GeradorCongLinear import GeradorCongLinear

SIZE_OF_ARRAY = 2000

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

def callLinearGenerator(gerador, a_value, c_value, mod_value):
  # -- generate seed values
  gerador.setSize(SIZE_OF_ARRAY)
  gerador.setMod(mod_value)
  gerador.generate(a_value, c_value)
  
  generated_values = gerador.getGeneratedValues()
  return generated_values

def calculateValues(values):
  # -- calulate and print results
  average.setTimes(SIZE_OF_ARRAY)
  average.calculate(values)

  standard_deviaton.setTimes(SIZE_OF_ARRAY)
  standard_deviaton.calculate(values, average.getValue())

  covariance.setTimes(SIZE_OF_ARRAY)
  covariance.calculate(values)

  quiSquare.setTimes(SIZE_OF_ARRAY)
  quiSquare.calculate(values)

def part_01():
  exercise_01()

def exercise_01():
  gerador = GeradorCongLinear()
  values = callLinearGenerator(gerador, 45, 1, 1024)

  plotter.plot(gerador.get_position_array(), 'o', color='black')
  plotter.show()

  calculateValues(values)
  printAllValues()

part_01()


