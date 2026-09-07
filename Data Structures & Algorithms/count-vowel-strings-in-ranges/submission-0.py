class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        valid = []
        prefixes = [0]
        output = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        prefix = 0

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                valid.append(1)
            else:
                valid.append(0)
        
        for i in range(len(valid)):
            prefix += valid[i]
            prefixes.append(prefix)
        
        for query in queries:
            output.append(prefixes[query[-1] + 1] - prefixes[query[0]])

        
        return output
        
        

        