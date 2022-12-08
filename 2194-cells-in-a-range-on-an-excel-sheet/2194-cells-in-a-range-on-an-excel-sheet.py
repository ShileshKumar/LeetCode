class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans=[]
        for i in range(ord(s[0]),ord(s[3])+1):
            res=""
            for j in range(int(s[1]),int(s[4])+1):
                rs=chr(i)+str(j)
                ans.append(rs)
        return ans