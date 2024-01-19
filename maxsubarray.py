def maxSubArray(nums):
    max_sub, currSum = nums[0],0

    for n in nums:
        if currSum<0:
            currSum = 0
        else:
            currSum+=n
            max_sub = max(max_sub, currSum)
        
    return max_sub

nums = [1,2,3,-9,4,-10]
print(maxSubArray(nums))


# if -2 > -3:
#     print("saad")
# else:
#     print("zehra")

