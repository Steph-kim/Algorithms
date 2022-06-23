/**
 * @param {number[]} prices
 * @return {number}
 */
 var maxProfit = function(prices) {
    let start = prices[0]
    let max = 0
    let curr
    
    for (let i=0; i<prices.length; i++) {
        curr = prices[i] - start
         start = Math.min(start, prices[i])
         max = Math.max(max, curr)
    }
     return max
     
 };