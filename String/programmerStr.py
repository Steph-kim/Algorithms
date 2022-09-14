def programmerStrings(str):

    # Assumption: There is exactly two guaranteed programmer strings
    def detect_programmer(str):
        set = {"p","r","o","g","a","m","e"}
        rCount = 2
        mCount = 1
        i = 0
        while len(set) != 0 or (rCount > 0 or mCount > 0):
            if (str[i] in set):
                set.remove(str[i])
            else:
                if (str[i] == "r"):
                    rCount -= 1
                elif (str[i] == "m"):
                    mCount -= 1
            i += 1
        return str[i::]
        
    str = detect_programmer(str)
    str = detect_programmer(str[::-1])

    return len(str)


str1 = "progxrammerrxprogxgrammer"
print(programmerStrings(str1))

str2 = "programmerxxxprozmerqgram"
print(programmerStrings(str2))

str3 = "programmerprogrammer"
print(programmerStrings(str3))

str4 ="psadfhjajsfhlakasrogammerajsrdfhasudfhasprogrammeeweqfdsafasdfasfdr"
print(programmerStrings(str4))

str5 = "programprogramprogrammerxxxxprogrammer"
print(programmerStrings(str5))

str = ""

