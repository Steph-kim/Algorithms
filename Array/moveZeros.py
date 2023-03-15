def function1(a):
    c = 0
    for i in range(len(a)):
        if a[i] == 0:
            c += 1
        elif c > 0:
            temp = a[i]
            a[i] = 0
            a[i-c] = temp

    return