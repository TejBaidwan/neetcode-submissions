class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)

        for word in strs:
            occurence = [0] * 26

            for letter in word:
                occurence[ord(letter) - ord("a")] += 1
            
            collection[tuple(occurence)].append(word)
        
        return list(collection.values())

