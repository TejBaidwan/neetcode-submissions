class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        collection = []

        for char in s:
            if char in opening:
                collection.append(char)

            elif char in closing:
                if not collection:
                    return False

                if opening.index(collection[-1]) != closing.index(char):
                    return False

                collection.pop()

        return len(collection) == 0
