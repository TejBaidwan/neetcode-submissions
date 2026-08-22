class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}

        for index, letter in enumerate(s):
            freq1[letter] = freq1.get(letter, 0) + 1
        
        for index, letter2 in enumerate(t):
            freq2[letter2] = freq2.get(letter2, 0) + 1
        
        return freq1 == freq2