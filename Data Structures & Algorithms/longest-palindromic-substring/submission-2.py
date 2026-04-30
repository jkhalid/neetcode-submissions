class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        max_substring = ''
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j + 1]
                if self.is_palindrome(substring) and len(substring) > len(max_substring):
                    max_substring = substring
        return max_substring

    def is_palindrome(self, substring: str) -> bool:
        left = 0
        right = len(substring) - 1

        while left < right:
            if substring[left] != substring[right]:
                return False
            left += 1
            right -= 1
        return True    