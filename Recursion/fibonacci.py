def fibonacci_recursive(n):

    if (n==0): return 0
    if (n==1): return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):

    a, b, c = 0, 1, 0

    if (n==0): return 0
    
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c 

    return b

# This method of calculating the fibonacci number is based off the iterative method above.
# For n-1 iterations, we repeat the following operation: a, b = b, a+b 
# and finally return b after n-1 iterations
# We can simplify this repetitive re-assignment by correspondingly changing the values of a and b in the recursive approach.
def fibonacci_tail_recursion(n, a=0, b=1):

    if (n==0): return a
    if (n==1): return b

    return fibonacci_tail_recursion(n-1, b, a+b)



n=7
print(fibonacci_recursive(n))
print(fibonacci_iterative(n))
print(fibonacci_tail_recursion(n))
