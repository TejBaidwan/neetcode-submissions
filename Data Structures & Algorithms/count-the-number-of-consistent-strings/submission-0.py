class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count = 0

        allowed_set = set(allowed)

        for word in words:
            word_set = set(word)

            if word_set.issubset(allowed_set):
                count += 1
        
        return count



