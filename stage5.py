# Zach Jewett
# CSCI443 - Stanley
# December 2, 2022
# Stage5 - Testing

import math

testList = ["#Clicks", "Task Time(s)", "#Pauses", "Pause Time(s)", "#Errors"]
optClicks = [10,1,4,12,3,1,1,5,2,5,4,1,2,3,1]

p1ClickArr = [10,1,6,12,3,1,1,5,4,5,4,1,2,3,1]
p1TaskTimeArr = [5.09,0.62,15.55,15.21,3.78,2.94,0.83,7.22,32.62,12.32,8.93,2.08,3.27,4.72,0.72]
p1PauseArr = [0,0,1,0,0,0,1,0,2,1,0,0,0,0,0]
p1PauseTimeArr = [0,0,3.78,0,0,0,1.27,0,22.6,3.42,0,0,0,0,0]
p1ErrorArr = [0,0,1,0,0,0,0,0,3,0,0,0,0,0,0]
p1Arrs =[p1ClickArr,p1TaskTimeArr,p1PauseArr,p1PauseTimeArr,p1ErrorArr]

p2ClickArr = [10,1,6,12,3,1,1,6,5,19,4,1,2,3]
p2TaskTimeArr = [10.36,2.99,18.32,12.93,4.93,1.85,1.89,11.8,31.28,45.5,10.32,2.42,2.32,3.57,1.01]
p2PauseArr = [0,1,1,0,0,0,0,1,2,4,1,0,0,0,0]
p2PauseTimeArr = [0,1.62,2.62,0,0,0,0,7.33,17.18,42.72,2.88,0,0,0,0]
p2ErrorArr = [0,0,0,0,0,0,0,0,3,3,0,0,0,0,0]
p2Arrs = [p2ClickArr,p2TaskTimeArr,p2PauseArr,p2PauseTimeArr,p2ErrorArr]

p3ClickArr = [4,1,6,12,3,1,1,6,22,32,12,1,2,3,4]
p3TaskTimeArr = [18.62,4.01,14.68,21.63,5.36,2.01,3.03,18.26,48.92,37.19,14.61,3.1,3.69,5.25,4.89]
p3PauseArr = [0,1,1,0,1,0,1,0,2,2,2,0,0,1,1]
p3PauseTimeArr = [0,3.07,2.82,0,2.03,0,1.57,0,62.74,67.89,12.4,0,0,2.64,0]
p3ErrorArr = [0,0,0,0,0,0,0,4,4,1,0,0,0,1]
p3Arrs = [p3ClickArr,p3TaskTimeArr,p3PauseArr,p3PauseTimeArr,p3ErrorArr]

p4ClickArr = [10,1,6,12,3,1,1,5,4,5,4,1,2,3,1]
p4TaskTimeArr = [5.21,1.37,13,14.98,3.55,0.89,0.86,5.49,4.33,10.96,6.67,1.91,3.03,3.28,0.68]
p4PauseArr = [0,0,0,0,0,0,0,0,1,1,0,0,0,0,0]
p4PauseTimeArr = [0,0,0,0,0,0,0,0,3.22,1.81,0,0,0,0,0]
p4ErrorArr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
p4Arrs = [p4ClickArr,p4TaskTimeArr,p4PauseArr,p4PauseTimeArr,p4ErrorArr]

p5ClickArr = [10,1,8,12,5,1,1,6,12,18,6,1,2,3,1]
p5TaskTimeArr = [13.78,2.21,17.6,18.6,5.01,1.77,1.83,16.57,27.8,19.43,14.54,2.21,4.36,4.46,3.78]
p5PauseArr = [1,0,0,0,1,0,1,1,1,1,1,0,1,1,1]
p5PauseTimeArr = [2.89,0,0,0,2.21,0,2.31,4.51,37.9,4.69,4.41,0,2.25,1.17,1.32]
p5ErrorArr = [0,0,0,0,1,0,0,0,1,1,1,0,0,0,0]
p5Arrs = [p5ClickArr,p5TaskTimeArr,p5PauseArr,p5PauseTimeArr,p5ErrorArr]


class UsabilityResults:
    def __init__(self, name, clickArr, taskTimeArr, pauseArr, pauseTimeArr, errorArr):
        self.particpant = name
        self.clicks = clickArr
        self.taskTimes = taskTimeArr
        self.pauses = pauseArr
        self.pauseTimes = pauseTimeArr
        self.errors = errorArr
        self.totals = [];

    def findTotals(self, useTest):
        sum = 0;
        for x in useTest:
            sum += x
        self.totals.append(sum)

    def findSum(self, useTest):
        sum = 0;
        for x in useTest:
            sum += x
        return sum

    def findMean(self, useTest):
        sum = self.findSum(useTest)
        mean = sum / 15.0
        return mean

    def findVariance(self, useTest):
        varianceSum = 0
        mean = self.findMean(useTest)
        for x in useTest:
            variance = x - mean
            variance = pow(variance, 2)
            varianceSum += variance
        return varianceSum

    def findStandardDeviation(self, useTest):
        var = self.findVariance(useTest)
        stdDev = math.sqrt(var)
        return stdDev

    def findErrorDiff(self):
        sum = 0
        iter = 0
        for x in self.clicks:
            diff = x - optClicks[iter]
            sum += diff
        optDiff = self.totals[0] - sum
        errPercent = optDiff / self.totals[0]
        return errPercent

    def displayResults(self):
        clickMean = self.findMean(self.clicks)
        clickMean = str(round(clickMean,2))
        timeMean = self.findMean(self.taskTimes)
        timeMean = str(round(timeMean,2))
        clickStdDev = self.findStandardDeviation(self.clicks)
        clickStdDev = str(round(clickStdDev,2))
        timeStdDev = self.findStandardDeviation(self.taskTimes)
        timeStdDev = str(round(timeStdDev,2))
        errDif = self.findErrorDiff()

        print(self.particpant, " performed an average of ", clickMean, " clicks with a standard deviation of ", clickStdDev)
        print(self.particpant, " performed an average of ", timeMean, " clicks with a standard deviation of ", timeStdDev)
        # print(self.particpant, " had an error difference of ", errDif, " off of optimal performance")

def findAllTotals(pArr):
    for p in pArr:
        x = 0
        while x < 5:
            p.findTotals(p1Arrs[x])
            x += 1


def displayAll(pArr):
    for p in pArr:
        p.displayResults()

def main():
    p1 = UsabilityResults("Amanda",p1ClickArr,p1TaskTimeArr,p1PauseArr,p1PauseTimeArr,p1ErrorArr)
    p2 = UsabilityResults("Laura",p2ClickArr,p2TaskTimeArr,p2PauseArr,p2PauseTimeArr,p2ErrorArr)
    p3 = UsabilityResults("Staci",p3ClickArr,p3TaskTimeArr,p3PauseArr,p3PauseTimeArr,p3ErrorArr)
    p4 = UsabilityResults("Forrest",p4ClickArr,p4TaskTimeArr,p4PauseArr,p4PauseTimeArr,p4ErrorArr)
    p5 = UsabilityResults("Ron",p5ClickArr,p5TaskTimeArr,p5PauseArr,p5PauseTimeArr,p5ErrorArr)
    particpantArr = [p1, p2, p3, p4, p5]
    findAllTotals(particpantArr)
    displayAll(particpantArr)


main()