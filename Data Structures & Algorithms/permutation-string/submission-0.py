class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        frequency = {}
        window = {}
        l = 0
        r = len(s2)

        for char in s1:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        for r in range(len(s2)):
            substring = (r - l) + 1

            window[s2[r]] = window.get(s2[r], 0) + 1

            if substring > len(s1):
                if window[s2[l]] <= 1:
                    window.pop(s2[l])
                else:
                    window[s2[l]] -= 1
                
                l += 1

            if frequency == window:
                return True

        return False
            
            
