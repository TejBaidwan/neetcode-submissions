class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_text = "".join(char for char in s if char.isalnum())

        for i in range(len(clean_text)):
            if clean_text[i].lower() != clean_text[-(i+1)].lower():
                return False
        
        return True
        