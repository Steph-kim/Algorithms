/**
 * @param {number[]} nums
 * @return {number}
 */
 var minDiff = function(nums) {
    nums.sort((a,b) => a-b);
    var r = 0
    for (let i=1; i<nums.length; i++) {
        c = Math.abs(nums[i]-nums[i-1])
        r += c
    }
    return r
};

let arr1 = [1,3,3,2,4]
console.log(minDiff(arr1))