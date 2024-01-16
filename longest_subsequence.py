def lengthOfLongestSubstring(s: str):
    hashset = set()
    start = 0
    max_length= 0 
    
    for i in range(len(s)):
        while s[i] in hashset:
            hashset.remove(s[start])
            start+=1
            
        hashset.add(s[i])
        
    
    # print(hashset)
    max_length = max(max_length, i - start + 1)
    print(max_length)


lengthOfLongestSubstring(s='abcabcab')