def twoSum(nums: list[int], target: int) -> list[int]:
    
    prevMap = {} # val:index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        else:
            prevMap[n]=i      # add number to hashmap like {n : i}
    return
        
    
nums = [2,7,11,15] 
target = 9

print(twoSum(nums, target))