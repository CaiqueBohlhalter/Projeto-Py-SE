class Covariance():
    
    def __init__(self) -> None:
        self.times = 10
        self.covariance = None
        self.covarianceAlternative = None

    def calculate(self, generatedNums):
        self.covariance = self.calculateCovariance(self.times, generatedNums)
        return self.covariance

    def calculateAlternative(self, generatedNums, average):
        self.covarianceAlternative = self.calculateCovarianceAlternative(self, self.times, generatedNums, average)
        return self.covarianceAlternative
    
    def calculateCovariance(self, times, generatedNums):
        sumX = 0

        for i in range(2, len(generatedNums)):
            sumX += generatedNums[i]

        sumY = 0

        for i in range(2, len(generatedNums)):
            if(i < len(generatedNums) - 1):
                sumY += generatedNums[i+1]

        averageX = sumX / times
        averageY = sumY / times
  
        valueX = 0
        valueY = 0
        value = 0

        for i in range(0, len(generatedNums), 2):
            valueX = generatedNums[i] - averageX
            valueY = generatedNums[i+1] - averageY
  
            value += (valueX - valueY) / ((times/2) - 1)
        
        covariance = value

        return covariance

    def calculateCovarianceAlternative (times, generatedNums, average):
        sumXY =  0
        sumX =  0
        sumY =  0

        for i in range(2, len(generatedNums), 2):
          sumXY += (generatedNums[i] * generatedNums[i+1])

        for i in range(2, len(generatedNums), 2):
            sumX += generatedNums[i]
        
        for i in range(2, len(generatedNums), 2):
            sumY += generatedNums[i+1]

        covarianceAlternative = (sumXY - (sumX * sumY)) / (times*(times-1));

        return covarianceAlternative
    
    def print(self):
        print(f"\nCovariancia: {self.covariance}")
    
    def printAlternative(self):
        print(f"\nCovariancia: {self.covarianceAlternative}")

    def printResult(self):
        print(f"\nCovariancia: {self.covariance}")

    def setTimes(self, times):
        self.times = times

    def getValue(self):
        return self.covariance

    def getValueAlternative(self):
        return self.covarianceAlternative
