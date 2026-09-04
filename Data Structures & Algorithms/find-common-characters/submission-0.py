class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        freq = {}

        for letter in words[0]:
            freq[letter] = freq.get(letter, 0) + 1

        for i in range(1, len(words)):
            word_freq = {}

            for letter in words[i]:
                word_freq[letter] = word_freq.get(letter, 0) + 1

            for key in freq:
                if key not in word_freq:
                    freq[key] = 0
                else:
                    freq[key] = min(freq[key], word_freq[key])

        result = []

        for key, value in freq.items():
            for _ in range(value):
                result.append(key)

        return result
