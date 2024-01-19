def gcdOfStrings(str1: str, str2: str) -> str:
    # Check if concatenated strings are equal or not, if not return ""
    if str1 + str2 != str2 + str1:
        return ""
    # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
    from math import gcd
    
    
    temp = gcd(len(str1), len(str2))
    print(temp)
    # return str1[:gcd(len(str1), len(str2))]
    str3 = str1[0:temp]
    print(str3)
    
    return str3
    
    
    
    
gcdOfStrings(str1="ABCABC", str2="ABC")