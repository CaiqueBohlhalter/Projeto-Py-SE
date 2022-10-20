from numpy import log as ln

class Ts():
  def __init__(self) -> None:
    self.ts = 10
    self.tsArray = []
  
  def calculate(self, generatedNums, a, b):
    return self.calculateTs(generatedNums, a, b)

  def calculateTs(self, generatedNums, a, b):
    #TS(i) = (b-a)(randon(i)) + a
    #Usaremos Impares para TEC

    for i in range(1, len(generatedNums), 2):
      self.tsArray.append((b-a) * (generatedNums[i]) + a) 

    return self.tsArray
 