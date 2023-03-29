class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j=len(haystack)
        n=len(needle)
        for i in range(j-n+1):
            if haystack[i:i+n]==needle:
                return i
        return -1
