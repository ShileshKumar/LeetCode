class Solution:
    def average(self, salary: List[int]) -> float:
        n=len(salary)
        mn=min(salary)
        salary.remove(mn)
        mx=max(salary)
        salary.remove(mx)
        res=sum(salary)/(n-2)
        return res