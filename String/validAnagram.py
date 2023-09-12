from collections import defaultdict

def groupAnagrams(strs):
    d = defaultdict(list)

    for str in strs:
        key = "".join(sorted(str))
        d[key].append(str)

    return list(d.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
