class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        
        left = 0
        right = len(cleaned) - 1
        while right > left:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True