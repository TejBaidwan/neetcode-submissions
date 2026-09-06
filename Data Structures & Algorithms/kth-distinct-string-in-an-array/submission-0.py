class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        freq = {}

        for item in arr:
            freq[item] = freq.get(item, 0) + 1

        for item in arr:
            if freq[item] == 1:
                k -= 1
                if k == 0:
                    return item

        return ""

