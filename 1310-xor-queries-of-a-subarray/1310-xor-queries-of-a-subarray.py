class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre=[]
        for i in range(len(arr)):
            if i==0:
                pre.append(arr[i])
            else:
                pre.append(arr[i]^pre[-1])
        op=[]
        for i in queries:
            if i[0]==0:
                op.append(pre[i[1]])
            else:
                op.append(pre[i[1]]^pre[i[0]-1])
        return op