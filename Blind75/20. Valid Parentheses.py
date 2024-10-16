# class Solution:
    # def isValid(self, s: str) -> bool:
def isValid(s):
    stack = []
    parentheses = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        elif c in [')', ']', '}']:
            if len(stack) == 0:
                return False
            p = stack.pop()
            if parentheses[p] != c:
                return False
    return len(stack) == 0