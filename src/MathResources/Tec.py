from numpy import log as ln

class Tec():
  def __init__(self) -> None:
    self.tec = 10
    self.tecArray = []
  
  def calculate(self, generatedNums):
    return self.calculateTec(generatedNums)

  def calculateTec(self, generatedNums):
    #TEC(i) = - 20 ln(randon(i))
    #Usaremos Pares para TEC

    for i in range(0, len(generatedNums) , 2):
      self.tecArray.append(-20 * (ln(generatedNums[i]))) 

    return self.tecArray