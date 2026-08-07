class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_copy = []
        for c in s:
            if c.isalnum():
                s_copy.append(c.lower())

        s_str = ''.join(s_copy)
        return s_str == s_str[::-1]
        