def isAnagram( s: str, t: str) -> bool:
        
        
    s= sorted(s)
    t= sorted(t)
    
    if s==t:
        return True
    
    else:
        return False
        
    
    
out = isAnagram("rac", "car")

print(out)