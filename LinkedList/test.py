def addOne(input):
    index = len(input)-1
    
    while index >= 0 and input[index] == 9:
        input[index] = 0
        index -= 1
        
    if index < 0: 
        input.insert(0,1)
    else:
        input[index] += 1

    return input
    
print(addOne([9,9,]))