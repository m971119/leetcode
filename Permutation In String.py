# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    count1, count2 = [0] * 26, [0] * 26
    for i in range(len(s1)):
        count1[ord(s1[i]) - ord("a")] += 1
        count2[ord(s2[i]) - ord("a")] += 1
    # calculate the initial matches
    matches = 0
    for i in range(26):
        if (count1[i] == count2[i]):
            matches += 1
    # slide the window to update the matches
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True
        # slide the window right: count the rightest char of the new window and update matches
        index = ord(s2[r]) - ord("a")
        count2[index] += 1
        if count1[index] == count2[index]:
            matches += 1
        elif count1[index] + 1 == count2[index]:
            # previous matched index should be deducted
            matches -= 1
        # remove the leftest char of the previous window and update matches
        index = ord(s2[l]) - ord("a")
        count2[index] -= 1
        if count1[index] == count2[index]:
            matches += 1
        elif count1[index] - 1 == count2[index]:
            # previous matched index should be deducted
            matches -= 1
        l += 1
    return matches == 26

    
checkInclusion("ab", "lecabee")


"""
update the matches of the characters of s1, find out if there is a window which the all 26 characters match the same frequency
https://pasteboard.co/nXcURndYsRlb.png
"""