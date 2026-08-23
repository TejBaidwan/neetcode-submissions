class Solution:
    def isValid(self, s: str) -> bool:
      
        pairs = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
        }

        stack = []

        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack or pairs[stack[-1]] != i:
                    return False
                stack.pop()

        return len(stack) == 0