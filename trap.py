# class Solution:
#     def trap(self, height: List[int]) -> int:
def trap(height) -> int:
    # check the maxLeftHeight and maxRightHeight
    # if either is < than currentHeight => no water trapped
    # else:
    #   height = min(maxLH, maxRH)
    #   result += height - currentHeight
    l = 0
    r = len(height) - 1
    maxLeft = height[l]
    maxRight = height[r]
    result = 0
    while (l < r):
        if maxLeft < maxRight:
            l += 1
            maxLeft = max(height[l], maxLeft)
            result += maxLeft - height[l]
        else:
            r -= 1
            maxRight = max(height[r], maxRight)
            result += maxRight - height[r]
    return result

