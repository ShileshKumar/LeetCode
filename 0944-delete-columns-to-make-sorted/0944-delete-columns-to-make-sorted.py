class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        co=0
        for i in range(len(strs[0])):
            l=[]
            for j in range(len(strs)):
                l.append(strs[j][i])
            if sorted(l)==l:
                continue
            else:
                co+=1
        return co