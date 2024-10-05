# class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
def productExceptSelf(nums):
    result = [1] * len(nums)
    # make the prefix array in memory
    for i in range(1, len(nums)):
        result[i] = result[i-1] * nums[i-1]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    return result


print(productExceptSelf([1, 2, 3, 4]))
"""
Prefix and Postfix
Data    | 1  | 2  | 3  | 4  |
prefix  | 1  | 2  | 6  | 24 |
postfix | 24 | 24 | 12 | 4  |
Result = prefix[i-1] * postfix[i+1]

# but you don't have to create the prefix and postfix arrays, you can solve this in memory
# 1. Make the result array the length of nums and contains all 1s
Result = [1, 1, 1, 1]
# 2. multiply prefix to the result
Result [1, 1, 2, 6]
# 3. make a postfix variable
postfix = 1
# 4. multiply this postfix var from the end of result
result = [1, 1, 2, 6*1]
postfix *= 4 (aka data[i]) == 4

result = [1, 1, 2*4, 6]
postfix *= 3 (aka data[i]) == 12

result = [1, 1*12, 8, 6]
postfix *= 2 (aka data[i]) == 24

result = [1*24, 12, 8, 6]
"""