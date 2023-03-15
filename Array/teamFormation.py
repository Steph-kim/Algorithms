def countTeams(ratings, queries):
    count = {}
    res = []
    for rating in ratings:
        if rating in count:
            count[rating] += 1
        else:
            count[rating] = 1
            
    for l, r in queries:
        subArray = ratings[l:r]
        teams = 0
        for i in range(len(subArray)):
            if count[subArray[i]] > 1:
                teams += 1;
                count[subArray[i]] -= 1
        res.append(teams)
    return res
    
ratings = [2,3,4,2]
queries = [[1,4], [3,4]]
print(countTeams(ratings, queries))

