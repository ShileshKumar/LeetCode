class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n=len(costs)
        costs.sort()
        cnt=0
        while cnt<n and costs[cnt]<=coins:
            coins=coins-costs[cnt]
            cnt=cnt+1
        return cnt