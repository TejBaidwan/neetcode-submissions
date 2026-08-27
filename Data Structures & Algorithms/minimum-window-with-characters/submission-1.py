class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        frequency = {}
        window = {}
        l = 0
        have = 0
        current_min = float('inf')
        best_start = 0

        for char in t:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        for i in range(len(s)):

            if s[i] in frequency:
                window[s[i]] = window.get(s[i], 0) + 1

                if frequency[s[i]] == window[s[i]]:
                    have += 1
            
            while have == len(frequency):
                substring = (i - l) + 1

                if substring < current_min:
                    current_min = substring
                    best_start = l

                if s[l] in frequency:
                    window[s[l]] -= 1

                    if window[s[l]] < frequency[s[l]]:
                        have -= 1

                l += 1

        if current_min == float('inf'):
            return ""

        return s[best_start:best_start + current_min]

                



