class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=''
        for i in digits:
            num+=str(i)
        res=int(num)+1
        ans=[]
        for i in str(res):
            ans.append(int(i))
        return ans