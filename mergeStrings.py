def mergeAlternately( word1: str, word2: str) -> str:
    temp=""
    i=0
    
    while i < min(len(word1), len(word2)):
        temp+=word1[i]
        temp+=word2[i]
        i+=1
        
    temp+= word1[i:]+word2[i:]
    
    return temp
    
    
mergeAlternately(word1="abcd", word2="pqr")
        