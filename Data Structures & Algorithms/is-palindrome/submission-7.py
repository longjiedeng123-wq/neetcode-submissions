class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        j = len(s) - 1
        i = 0
        while j > i:
            while j > i and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            j -= 1
            i += 1
        return True