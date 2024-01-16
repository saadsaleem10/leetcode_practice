def longestConsecutive(nums: list[int]) -> int:
    numSet = set(nums)
    longest = 0
    
    for n in nums:
        # print("checking for " + str(n))
        if (n-1) not in numSet:
            # print("no previous value for " + str(n))
            length=0
            while (n+length) in numSet:
                # print(str(n) + " has a next value!")
                length+=1
                
                
            longest=max(length,longest)
            
    return longest

nums = [100,4,200,1,3,2]

out = longestConsecutive(nums)

print(out)
            