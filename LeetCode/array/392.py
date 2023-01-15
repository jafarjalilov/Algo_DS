# https://leetcode.com/problems/is-subsequence/
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = 0
        if len(s) == 0:
            return True
        for i in t:
            if a >= len(s)-1 and i == s[a]:
                return True
            if i == s[a]:
                a += 1
        return False
"""

# BETTER SOLUTION WITH POINTER METHOD
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

object = Solution()
print(object.isSubsequence("abc", "ahbgdc"))
print(object.isSubsequence("axc", "ahbgdc"))