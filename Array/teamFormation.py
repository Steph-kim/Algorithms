def countTeams(rating, queries):

    res = []
    for l, r in queries:
        seen = {}
        teams = 0
        if r <= len(rating):
            for i in range(l-1, r):
                if rating[i] != 0:
                    if rating[i] in seen and rating[i] != 0:
                        teams += 1
                        index = seen[rating[i]]
                        seen.pop(rating[i])
                        rating[index] = 0
                        rating[i] = 0
                    else: 
                        seen[rating[i]] = i
        res.append(teams)
    return res
    
rating=  [8, 8, 10, 1, 4, 5, 8, 10, 7, 6, 8, 3, 2, 5, 2, 3, 1, 8, 7, 7, 7, 3, 4, 2, 2, 3, 5, 10, 1, 10, 8, 7, 4, 5, 1, 4, 4, 5, 6, 2, 10, 7, 1, 7]
queries= [[43, 44], [2, 36], [21, 26], [37, 43], [29, 43], [34, 36], [26, 27], [35, 42], [14, 34], [23, 44], [36, 41], [17, 37], [42, 45], [5, 35], [18, 34], [16, 17]]
print(countTeams(rating, queries))


"""
 0  s                            10                            20                              30             e              40        43
[8, 0, 00, 0, 0, 0, 0, 00, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 00, 0, 00, 8, 7, 0, 0, 0, 0, 4, 5, 6, 2, 10, 7, 1, 7]
teams = 16

res = [0, 16, 0, 0]


"""