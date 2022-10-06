import math

class StandardDeviaton():
    
    def __init__(self) -> None:
      self.times = 10
      self.standardDeviation = None
        

    def calculate(self, generatedNums, average):
        return self.calculateStandardDeviation(self.times, generatedNums, average)

    def calculateStandardDeviation(self, times, generatedNums, average):
        sum = 0
        
        for i in range(2,len(generatedNums)):
            sum += math.pow((generatedNums[i] - average),2)

        self.standardDeviation = math.sqrt(sum / (times-2))
    
        return self.standardDeviation

    def printResult(self):
        print(f"\nDesvio Padrão: {self.standardDeviation}")

    def setTimes(self, times):
        self.times = times

    def getValue(self):
        return self.standardDeviation
