class Average():
    
    def __init__(self) -> None:
      self.times = 10
      self.average = None
        
    def calculate(self, generatedNums):
        return self.calculateAverage(self.times, generatedNums) 
    
    def calculateAverage(self, times, generatedNums):
        sum = 0
    
        for i in range(len(generatedNums)):
            sum += generatedNums[i]
  
        self.average = sum/(times)
        return self.average

    def printResult(self):
        #print("\nMédia: " + str(self.average))
        print(f"\nMédia: {self.average}" )

    def setTimes(self, times):
        self.times = times

    def getValue(self):
        return self.average