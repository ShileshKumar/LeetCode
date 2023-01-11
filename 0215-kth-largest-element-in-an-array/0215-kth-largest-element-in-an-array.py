class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]
        for i in nums:
            heappush(minHeap,i)
            if len(minHeap)>k:
                heappop(minHeap)
        return minHeap[0] #top element is the kth largest element in the array