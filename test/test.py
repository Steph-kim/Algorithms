def func1(arr): 
    subarray = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            subarray.append(arr[i:j])
        
    print(subarray)
    res = 0
    for arr in subarray:
        res += len(set(arr))

    return res

# arr = [1,2,3,1,1,1]
# print(func1(arr))



"""

----------------
  [1] = 1
  
  [1,1] = 3
  [1,2] = 4

  [1,1,1] = 6
  [1,2,1] = 9
  [1,2,3] = 10

  [1,1,1,1] = 10
  [1,2,1,1] = 15
  [1,2,3,1] = 19
  [1,2,3,4] = 20

  [1,1,1,1,1] = 15
  [1,2,1,1,1] = 22
  [1,2,3,1,1] = 29
  [1,2,3,4,1] = 34
  [1,2,3,4,5] = 35

  .
  .
  [1,2,3,1,1,1] = 40
  [1,2,3,4,1,1] = 49
  [1,2,3,4,5,1] = 55
  [1,2,3,4,5,6] = 56


"""

# def calculate_n(i):
#     n = 0
#     for j in range(i + 1):
#         n += j * (j + 1) // 2
#     return n

# i = 7
# n = calculate_n(i)
# print(f"When i = {i}, n = {n}")



def func2():
    return

def func1():
    return

def func1():
    return

def sumoflength(arr, n):
 
    # For maintaining distinct elements.
    s = []
 
    # Initialize ending point and result
    j = 0
    ans = 0
 
    # Fix starting point
    for i in range(n):
         
        # Find ending point for current
        # subarray with distinct elements.
        while (j < n and (arr[j] not in s)):
            s.append(arr[j])
            j += 1
 
        # Calculating and adding all possible
        # length subarrays in arr[i..j]
        ans += ((j - i) * (j - i + 1)) // 2
 
        # Remove arr[i] as we pick new
        # starting point from next
        s.remove(arr[i])
 
    return ans

arr = [1,2,1]
n = len(arr)
print(sumoflength(arr, n))