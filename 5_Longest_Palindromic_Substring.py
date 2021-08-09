class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        indices = [0, 0]
        for i in range(len(s)):
            self.palindrome(s, i, i, indices)
            self.palindrome(s, i, i + 1, indices)
        return s[indices[0]: indices[1] + 1]

    def palindrome(self, s, left, right, indices):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        left += 1
        right -= 1
        if right - left > indices[1] - indices[0]:
            indices[0], indices[1] = left, right
