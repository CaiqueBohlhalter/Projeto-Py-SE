class Average:
    
    def __init__(self) -> None:
      self.times = 10
      self.average = None
        
    def calculate(self, generatedNums):
        return self.calculateAverage(self.times, generatedNums) 
    
    def calculateAverage(self, times, generatedNums):
        sum = 0
    
        for i in range(2, len(generatedNums)):
            sum += generatedNums[i]
  
        self.average = sum/(times-2)
        return self.average

    def printResult(self):
        print("\nMédia: " + self.average)

    def setTimes(self, times):
        self.times = times

    def getValue(self):
        return self.average