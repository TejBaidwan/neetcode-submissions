class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        seen = {}
        longest = 0

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1

            max_frequency = max(seen.values())
            window = r - l + 1

            while window - max_frequency > k:
                seen[s[l]] -= 1
                l += 1

                window = r - l + 1
                max_frequency = max(seen.values())

            longest = max(longest, r - l + 1)

        return longest