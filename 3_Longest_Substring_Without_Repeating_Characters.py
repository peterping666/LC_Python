class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not str:
            return 0
        res = 0
        unique = set()
        left = 0
        for right in range(len(s)):
            char = s[right]
            while char in unique:
                unique.remove(s[left])
                left += 1
            unique.add(char)
            res = max(res, right - left + 1)
        return res