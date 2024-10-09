import math




def main():
    #An array of a stock's past prices taken on the first of every month
    stockPast = [0,.01,1.43,2,5,8,10,8,12,7,2]
    isGoodInvestment(stockPast)

#Calculates the percent growth of a stock starting at a specific month
def calcFutureValue(pastValue,startSpot = 0,):
    growthSinceStart = 0
    sum = 0
    for i in range(startSpot,len(pastValue)):
        sum += pastValue[i]
    growthSinceStart = sum / len(pastValue)
    return growthSinceStart

def isGoodInvestment(stockPast):
    totalGrowth = [calcFutureValue(stockPast),1]
    halfRecentGrowth = [calcFutureValue(stockPast,math.floor(len(stockPast) / 2)),2]
    quarterRecentGrowth = [calcFutureValue(stockPast,math.floor(len(stockPast) / 4)),3]
    lastMonthGrowth  = [calcFutureValue(stockPast,(len(stockPast)-1)),5]

    print(totalGrowth)
    print(halfRecentGrowth)
    print(quarterRecentGrowth)
    print(lastMonthGrowth)


if __name__ == '__main__':
    main()