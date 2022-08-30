class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=j=0
        x=0
        d=set()
        for j in range(len(s)):
            while s[j] in d:
                d.remove(s[i])
                i+=1
            d.add(s[j])
            x=max(x,j-i+1)
        return x
                