def containsDuplicate( nums: list[int]) -> bool:
    numSet = set()
    
    for n in nums:
        # print("checking " + str(n))
        if n not in numSet:
            # print("adding " + str(n) + " to set")
            numSet.add(n)
        else:
            return True
        
    return False
