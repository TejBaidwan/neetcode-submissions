class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        l = 0
        output = []
        hashmap = {}
        max_last_index = 0

        for i in range(len(s)):
            hashmap[s[i]] = i

        for i in range(len(s)):
            max_last_index = max(max_last_index, hashmap[s[i]])

            if i == max_last_index:
                output.append(i - l + 1)
                l = i + 1
                max_last_index = 0

        return output




