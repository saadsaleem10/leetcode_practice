def maxProd(nums):
    min_prod = max_prod = ans = nums[0]

    for value in nums[1:]:
        min_temp = min_prod*value
        max_temp = max_prod*value

        min_prod = min(value, min_temp, max_temp)
        max_prod = max(value, min_temp, max_temp)

        ans = max(ans, max_prod)

    return ans


nums = [2, -2, 2, -2]

print(maxProd(nums))