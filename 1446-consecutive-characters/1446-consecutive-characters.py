class Solution:
    def maxPower(self, s):
        ans, streak = 1, 1
        n=len(s)
        for i in range(1,n):
            if s[i] == s[i-1]:
                streak+=1
                ans = max(ans,streak);
            else: 
                streak = 1
        return ans