/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxProduct = function(nums) {
    var max = nums[0];
    var minProdEnding = nums[0];
    var maxProdEnding = nums[0];
    
    for (let i=1; i<nums.length; i++) {
        var a = Math.min(nums[i], minProdEnding*nums[i], maxProdEnding*nums[i])
        var b = Math.max(nums[i], minProdEnding*nums[i], maxProdEnding*nums[i])
        minProdEnding = a
        maxProdEnding = b
        max = Math.max(max, maxProdEnding)
    }
    return max
};