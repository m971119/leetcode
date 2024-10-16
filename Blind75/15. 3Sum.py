# class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
def threeSum(nums):
    # sum = 0
    nums.sort()
    # [-4, -1, -1, 0, 1, 2]
    result = []
    for i, num in enumerate(nums):
        if num > 0:
            break
        if i > 0 and num == nums[i-1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while(l < r):
            threeSum = num + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                result.append([num, nums[l], nums[r]])
                l += 1
                r -= 1
                while (nums[l] == nums[l-1]) and l < r:
                    l += 1

    return result

print(threeSum([-1,0,1,2,-1,-4]))


"""
Hint: First Sort the array
Hint: Two Pointer!
"""