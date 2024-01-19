def findMin(nums):
    l = 0
    r = len(nums)-1

    while l<r:
        m = (l+r)//2
        if nums[m]>nums[r]:
            l = m+1

        else:
            r=m

    return nums[m]


nums = [1,2,3,4,5]
print(findMin(nums))