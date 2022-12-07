class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        cnt1=0
        cnt0=0
        ans0=0
        ans1=0
        for i in s:
            if i=='1':
                cnt1+=1
                cnt0=0
            else:
                cnt0+=1
                cnt1=0

            ans0=max(ans0,cnt0)
            ans1=max(ans1,cnt1)
        return ans1>ans0