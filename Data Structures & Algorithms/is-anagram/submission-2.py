class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_s = {}
        dictionary_t = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            dictionary_s[s[i]] = 1 + dictionary_s.get(s[i], 0)
            dictionary_t[t[i]] = 1 + dictionary_t.get(t[i], 0)
        for j in dictionary_s:
            if dictionary_s[j] != dictionary_t.get(j, 0):
                return False
        
        return True
            