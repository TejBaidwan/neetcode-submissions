class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        shorter = min(word1, word2, key=len)
        longer = max(word1, word2, key=len)

        output = []

        for i in range(len(shorter)):
            output.append(word1[i])
            output.append(word2[i])

        output.append(longer[len(shorter):])

        return "".join(output)
