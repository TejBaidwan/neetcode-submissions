class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        frequency = {}
        total = 0

        for letter in chars:
            frequency[letter] = frequency.get(letter, 0) + 1

        for word in words:
            frequency_word = {}

            for letter in word:
                frequency_word[letter] = frequency_word.get(letter, 0) + 1

            can_form = True

            for letter, count in frequency_word.items():
                if frequency.get(letter, 0) < count:
                    can_form = False
                    break

            if can_form:
                total += len(word)

        return total
            

