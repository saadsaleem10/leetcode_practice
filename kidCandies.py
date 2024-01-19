# def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
#     boolean_array = [False] * len(candies)
#     new_candies = [0]* len(candies)
    
#     for i in range(len(candies)):
#         new_candies[i] = candies[i]+extraCandies
#         print(candies)
        
#         temp = max(candies)
#         print(temp)
        
#         if new_candies[i] >= temp:
#             boolean_array[i] = True
        
#         else:
#             boolean_array[i] = False
            
#     print(boolean_array)
            
#     return boolean_array


def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    m = max(candies)
    res = []
    for i in candies:
        if i + extraCandies >= m:
            res.append(True)
        else:
            res.append(False)
    print(res)
    return res
    
candies = [2,3,5,1,3] 
extraCandies = 3

kidsWithCandies(candies, extraCandies)

    