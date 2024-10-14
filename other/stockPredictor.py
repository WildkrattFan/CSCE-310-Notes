import math




def main():
    #An array of a stock's past prices taken on the first of every month
    stockPast = [150.32, 152.45, 149.87, 153.22, 148.76, 151.90, 150.78, 154.67, 155.23, 149.99]
    growthStandard = [1,1.2,1.3,1.4,1.5,1.5,1.6,1.7]

    isGoodInvestment(stockPast)
    #isGoodInvestment(stockPast)

#Calculates the percent growth of a stock starting at a specific month
def growthSinceStart(pastValue,startSpot = 0, endSpot = 100):
    monthToMonthGrowth = []
    averageMonthToMonthGrowth = 0
    startSpot += 1
    for i in range(startSpot, endSpot-1):
        if pastValue[i-1] > 0:
            monthToMonthGrowth.append((pastValue[i]/pastValue[i-1]))
        else: 
            print("Error, stock can not be valued at zero")
    for percent in monthToMonthGrowth:
        averageMonthToMonthGrowth += percent
    if len(monthToMonthGrowth) > 0:
        averageMonthToMonthGrowth = averageMonthToMonthGrowth/len(monthToMonthGrowth)
    else: 
        averageMonthToMonthGrowth = averageMonthToMonthGrowth
    return averageMonthToMonthGrowth

def findVolatility(pastValues):
    growthRates = []
    for i in range(1, len(pastValues)):
        growthRates.append((pastValues[i] - pastValues[i - 1]) / pastValues[i - 1])
    # Calculate standard deviation of the growth rates
    meanGrowth = sum(growthRates) / len(growthRates)
    variance = sum((x - meanGrowth) ** 2 for x in growthRates) / len(growthRates)
    return math.sqrt(variance)

def calculateSharpeRatio(stockReturn, riskFreeReturn, volatility):
    return (stockReturn - riskFreeReturn) / volatility

def compoundedGrowth(pastValues, startSpot=0, endSpot=100):
    startValue = pastValues[startSpot]
    endValue = pastValues[endSpot - 1]
    months = endSpot - startSpot
    if startValue > 0:
        return (endValue / startValue) ** (1 / months) - 1
    else:
        return 0

def isGoodInvestment(stockPast):
    totalGrowth = compoundedGrowth(stockPast)
    volatility = findVolatility(stockPast)
    sharpeRatio = calculateSharpeRatio(totalGrowth, 0.02, volatility)  # Assuming 2% risk-free rate
    
    print(f"Total Growth: {totalGrowth}, Volatility: {volatility}, Sharpe Ratio: {sharpeRatio}")
    
    # Decision-making criteria
    if sharpeRatio > 1 and totalGrowth > 1.05:
        return True
    return False



if __name__ == '__main__':
    main()