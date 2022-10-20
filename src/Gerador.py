class Gerador():

  def __init__(self) -> None:
    self.size = 10
    self.mod = self.mValue()
    self.seed =  10
    self.constant =  16807
    self.generatedValues = []
    self.usageValues = []

  def generate(self):
    self.generatedValues = [0 for i in range(self.size)]
    self.generateValue(self.seed, self.mod, self.constant)
  
  def mValue(self):
    mod = pow(2,31)
    mod = mod -1
    return mod
  
  def generateValue(self, seed, mod, constant):
    for i in range(self.size):
      self.generatedValues[i] = (seed / mod)
      seed = self.generator(seed, mod, constant)

    self.removeFirstThreeValues()

  def removeFirstThreeValues(self):
    for i in range(len(self.generatedValues)):
      if(i > 2):
        self.usageValues.append(self.generatedValues[i])

  def generator(self, seed, mod, constant):
    return (constant * seed) % mod

  def getGeneratedValues (self):
    return self.usageValues

  def setSize(self, size):
    self.size = size + 3

