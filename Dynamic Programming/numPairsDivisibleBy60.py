def numPairsDivisibleBy60(songs):
    count = [0] * 60
    res = 0

    for i in range(len(songs)):
        index = songs[i] % 60
        res += count[(60 - index) % 60] 
        count[index] += 1
    print(count)
    return res

test = [30,20,150,100,40]
print(numPairsDivisibleBy60(test))
test2 = [60,60,60]
print(numPairsDivisibleBy60(test2))
test3 = [60, 180]
print(numPairsDivisibleBy60(test3))
