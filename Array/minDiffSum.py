def minDiff(arr):
    arr.sort()
    minDiff = 0
    for i in range(len(arr)-1):
        currDiff = abs(arr[i+1] - arr[i])
        minDiff += currDiff
    return minDiff
    
arr1 = [1,3,3,2,4]
print(minDiff(arr1))

arr2 = [5,1,3,7,3]
print(minDiff(arr2))

arr3 = [4,1]
print(minDiff(arr3))
