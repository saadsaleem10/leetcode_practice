def productExceptSelf(nums: list[int])->list[int]:
    res = ([1] * len(nums))
    
    prefix = 1
    
    for i in range(len(nums)):
        res[i] = prefix
        print("array right now" + str(res))
        prefix *= nums[i]
        print("prefix right now" + str(prefix))
        
    postfix = 1
    
    for i in range(len(nums)-1, -1, -1):
        res[i]*=postfix 
        print("array right now" + str(res))
        postfix*=nums[i]
        print("postfix right now" + str(postfix))
        
    return res
        
    
print(productExceptSelf(nums=[4,2,3,5]))
    
    
        