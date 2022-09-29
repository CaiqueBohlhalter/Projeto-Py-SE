import math


class GeradorCongLinear:
    
    def __init__(self) -> None:
      self.size = 10
      self.mod = self.mValue()
      self.seed =  10
      self.constant = 16807
      self.generatedValues = []

    def generate(self, value_a, value_c):
        self.generatedValues = [0 for i in range(10)]
        self.generatedValues[0] = self.seed
  
        self.generateValue(value_a, value_c)

    def generateValue(self, value_a, value_c):
        
        for i in range(self.size):
            if(i < self.size - 1):
                self.generatedValues[i + 1] = self.fmod(self.generator(self.generatedValues[i], value_a, value_c), self.mod); 
            
            self.generatedValues[i] = self.generatedValues[i] / self.mod

    def fmod(self, a, b):
        result = math.floor(a / b)
        return a - result * b

    def mValue(self):
        mod = pow(2,31)
        mod = mod -1
        return mod

    def generator(self, seed, a, c):
        return (a * seed) + c

    def getGeneratedValues(self):
        return self.generatedValues
    
    def setSize(self, size):
        self.size = size

    def setMod(self, mod): 
        self.mod = mod
