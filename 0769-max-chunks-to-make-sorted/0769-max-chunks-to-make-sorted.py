class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        mx=[arr[0]]
        for i in range(1,n):
            mx.append(max(max(mx),arr[i]))
        #print(mx)
        arr.sort()
        #print(arr)
        cnt=0
        for i in range(n):
            if arr[i]==mx[i]:
                cnt+=1
        return cnt