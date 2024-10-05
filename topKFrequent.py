# class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:

def topKFrequent(nums, k):
    counts = {}
    for num in nums:
        counts[num] = 1 + counts.get(num, 0)
    freq = [[] for i in range(len(nums) + 1)]
    for num, count in counts.items():
        freq[count].append(num)
    result = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if (len(result) == k):
                return result









"""
# data = [1, 1, 2, 3]
1. make the count dict
# {1: 2, ,2: 1, 3: 1}
2. Bucket Sort
| count | 0  |    1   |  2  | 3 |
| value | [] | [2, 3] | [1] |   |
3. 由最大值(max count) 向下撈 k 個 items
"""

