import math

class QuiSquare():

    def __init__(self) -> None:
      self.intervals = 10
      self.mod = self.mValue()
      self.times = 100000
      self.qCarry = [0 for i in range(self.times)]
      self.quiSquare = 0
        

    def calculate(self, generatedNums):
        return self.calculateQuiSquare(self.times, generatedNums)

    def calculateQuiSquare(self, times, generatedNums):
        isCondition1 = False
        isCondition2 = False
        counter = 0

        for i in range(self.intervals):
          for j in range(self.times):
            isCondition1 = (counter / self.intervals) < (generatedNums[j] / self.mod)
            isCondition2 = (generatedNums[j] / self.mod) <= ((counter + 1) / self.intervals)
            if(isCondition1 & isCondition2):
              self.qCarry[i] += 1

          self.quiSquare += math.pow(self.qCarry[i] - times / 10, 2) / (times / 10)
          counter += 1

        return self.quiSquare

    def mValue(self):
        mod = math.pow(2,31)
        mod = mod -1
        return mod

    def printResult(self):
        print(f"\nQui-Quadrado: {self.quiSquare}" )

    def setTimes(self, times):
        self.times = times

    def getValue(self):
        return self.quiSquare
