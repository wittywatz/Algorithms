def sherlockAndAnagrams(s):
    anagrams = {}
    for i in range(len(s)):
        for j in range(i,len(s)):
            temp = ''.join((sorted(s[i:j+1])))
            anagrams[temp] = anagrams.get(temp,0)+1
    count_anagrams = 0
    for value in anagrams.values():
        count_anagrams += ((value**2)-value)//2
  
    return count_anagrams