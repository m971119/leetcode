# class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0
    for n in nums:
        if (n-1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

print(longestConsecutive([100, 4, 200, 3, 2, 1]))


"""
The time complexity is O(n) because if the number isn't the start of the sequence
aka num-1 exists, we skip counting the sequence

so for the [100, 4, 200, 3, 2, 1] example
we only count when n is 100, 200 and 1! We skip 4, 3, 2
"""