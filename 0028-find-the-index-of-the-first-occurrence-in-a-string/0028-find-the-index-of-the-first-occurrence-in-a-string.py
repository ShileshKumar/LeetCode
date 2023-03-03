class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=len(haystack)
        l=len(needle)
        for i in range(h-l+1):
            if haystack[i:i+l]==needle:
                return i
        else:
            return -1
        