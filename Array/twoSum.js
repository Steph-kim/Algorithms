/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    let map = {}
    for (let i = 0; i < nums.length; i++) {
        let v = target - nums[i]
        if (map[v] >= 0) {
            return [i, map[v]]
        }
        map[nums[i]] = i    
    }
};