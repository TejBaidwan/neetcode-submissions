class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        longest = 0
        last_seen = {}

        for r in range(len(s)):
            if s[r] in last_seen:
                l = max(l, last_seen[s[r]] + 1)

            last_seen[s[r]] = r
            longest = max(longest, r - l + 1)

        return longest