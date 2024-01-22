def countPairs(nums: list[int], target: int) -> int:
    left = 0
    count  = 0
    right = len(nums)-1
    
    while left<right:
        if nums[left]+nums[right]<target:
            
            count = right-left
            left+=1
            
        else:
            right-=1
            
    return count


    