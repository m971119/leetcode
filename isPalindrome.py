# class Solution:
    # def isPalindrome(self, s: str) -> bool:
def isPalindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1
    while (True):
        while i < len(s) and not s[i].isalnum():
            i += 1
        while j >= 0 and not s[j].isalnum():
            j -= 1
        if (i >= j):
            break
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True
    
"""
implement isalnum() yourself
"""

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9'))