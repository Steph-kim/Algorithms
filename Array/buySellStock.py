def maxProfit(prices):
    maxProfit = 0
    minPrice = prices[0]
    
    for i in range(1, len(prices)):
        currPrice = prices[i] - minPrice
        
        minPrice = min(minPrice, prices[i])
        maxProfit = max(maxProfit, currPrice)
        
    return maxProfit