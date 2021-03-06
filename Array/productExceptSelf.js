/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var productExceptSelf = function(nums) {
    let res = new Array(nums.length).fill(1)
    let p = 1
    
    for (let i=0; i<nums.length; i++) {
        res[i] *= p
        p *= nums[i]
    } 

    p = 1
    for (let i=nums.length-1; i>= 0; i--) {
        res[i] *= p
        p *= nums[i]
    }
    
    return res
};