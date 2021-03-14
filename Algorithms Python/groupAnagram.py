def groupAnagrams(strs):
    same = {}
    for str in strs:
        key = "".join(sorted(str))
        if key not in same.keys():
            same[key] = []
        same[key].append(str)
        
    return [val for val in same.values()]
            
