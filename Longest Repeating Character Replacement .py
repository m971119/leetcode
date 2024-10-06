# class Solution:
    # def characterReplacement(self, s: str, k: int) -> int:
def characterReplacement(s: str, k: int) -> int:
    maxf = 0
    l = 0
    count = {}
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
    return r - l + 1
            
print(characterReplacement("AAABABB", 1))

"""
The whole purpose is to find the max frequency of characters (maxf) within the legal sliding windows, because the answer is (result_window_length - maxf)
下 breakpoint 觀查 s[l:r+1] 與 r - l + 1 關係，不更新 maxf 卻讓 l += 1 使 window_length 變短沒有關係，因為下一個 loop r 也會 += 1！


Neetcode Explanation: https://youtu.be/gqXU1UyA8pk
"""