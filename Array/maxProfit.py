def maxProfit(prices):

    minPrice = prices[0] 
    maxProfit = 0

    for i in range(1, len(prices)):
        profit = prices[i] - minPrice
        if (profit > maxProfit):
            maxProfit = profit
        elif (prices[i] < minPrice):
            minPrice = prices[i]
    
    return maxProfit
    
prices = [7,1,5,3,6,4]
print(maxProfit(prices))
    

