/**
 * @param {number[]} height
 * @return {number}
 */
 var maxArea = function(height) {
    let max = 0
    let l = 0, r = height.length-1;
    let area, minHeight, width;

    while (l < r) {
        minHeight = Math.min(height[l], height[r])
        width = r-l 
        area = minHeight*width
        max = Math.max(max, area)
        
        if (height[l] < height[r]) {
            l += 1
        } else { 
            r -= 1
        }
    }
    return max
};