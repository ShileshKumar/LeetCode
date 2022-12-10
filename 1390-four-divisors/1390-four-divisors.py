class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:  
        res=0
        for num in nums:
            divisor={1,num}
            for i in range(2,int(math.sqrt(num))+1):
                if num%i==0:
                    divisor.add(num//i)
                    divisor.add(i)
                if len(divisor)>4:
                    break
            if len(divisor) == 4:            
                res+=sum(divisor)
        return res