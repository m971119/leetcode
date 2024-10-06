# class Solution:
#     def encode(self, strs: List[str]) -> str:
#     def decode(self, s: str) -> List[str]:

def encode(strs):
    result = ''
    for str in strs:
        result += f"{len(str)}#{str}"
    return result


def decode(s):
    # s[i:j] = the length of string
    # s[j] = the # sign
    i = 0
    result = []
    while (i < len(s)):
        j = i
        while (s[j] != '#'):
            j += 1
        result.append(s[j+1:j+1+int(s[i:j])])
        i = j + int(s[i:j]) + 1
    return result


en = encode(["we","say",":","yes","!@#$%^&*()"])
print(decode(en))


"""
Be Careful that the length of string might be >= 10
"""