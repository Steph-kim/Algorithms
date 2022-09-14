import builtins
from itertools import combinations

def function(array, K):
    dic = {}
    array = [a for a in array if a <= K]

    for i in range(len(array)):
        for combination in combinations(array, i + 1):
            if sum(combination) <= K:
                dic[sum(combination)] = combination
    return (list(dic))
print(function([5,4,3,2,1], 8))