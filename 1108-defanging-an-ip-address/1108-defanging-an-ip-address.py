class Solution:
    def defangIPaddr(self, address: str) -> str:
        n=len(address)
        ans=''
        for i in range(n):
            if address[i]=='.':
                ans=ans+'[.]'
            else:
                ans=ans+address[i]
        return ans
            