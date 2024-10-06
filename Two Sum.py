# class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
def twoSum(nums, target):
    num_index = {}
    for i in range(len(nums)):
        num = nums[i]
        remain = target - num
        if remain in num_index:
            return [num_index[remain], i]
        num_index[num] = i
            
