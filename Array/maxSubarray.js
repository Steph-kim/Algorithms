/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    let max = Number.NEGATIVE_INFINITY
    let lastEnding = 0
    
    for (let i=0; i<nums.length; i++) {
        lastEnding += nums[i]     
        max = Math.max(max, lastEnding)
        if (lastEnding < 0) {
            lastEnding = 0
        } 
    }
    return max  
};