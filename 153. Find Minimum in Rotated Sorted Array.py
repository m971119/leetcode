# class Solution:
    # def findMin(self, nums: List[int]) -> int:
def findMin(nums):
    # [3,4,5,6,1,2]
    # [1, 2]
    
    if nums[0] <= nums[-1]:
        return nums[0]
    if len(nums) == 2:
        return min(nums[0], nums[1])
    m = len(nums) // 2
    if nums[m] >= nums[0]:
        return findMin(nums[m:])
    else:
        return findMin(nums[0:m+1])


    
"""
Leetcode Top Solution
"""
def findMinLeetcode(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]