class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSD(num):
            if '0' in str(num):
                return False
            for i in str(num):
                if num%(int(i))!=0:
                    return False
            return True
        
        ans=[]
        for i in range(left,right+1):
            if isSD(i)==True:
                ans.append(i)
        return ans
            