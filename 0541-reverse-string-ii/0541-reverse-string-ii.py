class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=""
        for i in range(0,len(s),2*k):
            p=s[i:i+k]
            p=p[::-1]
            ans+=p
            ans+=s[i+k:i+2*k]
        return ans