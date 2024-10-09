# class Solution:
    # def search(self, nums: List[int], target: int) -> int:
def search(nums, target: int) -> int:
    # [4, 5, 6, 7, 0, 1, 2] 找 1
    # 左 sorted -> 且 target < 左[0] -> 找右 array
    # [2, 4, 5, 6, 7, 0, 1] 找 7
    # 左 sorted -> 且 target > mid -> 找右 array
    # [2, 4, 5, 6, 7, 0, 1] 找 4
    # 左 sorted 且 左[0] < target < mid -> 找左 array
    # [6, 7, 0, 1, 2, 4, 5] 找 5
    # 左 unsorted 且 target < nums[mid] -> 找左 array
    # [6, 7, 0, 1, 2, 4, 5] 找 5
    # 左 unsorted 且 target > nums[r] -> 找左 array
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        # left array is sorted!
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # left array isn't sorted
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1


