class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        if n<=1:
            return [0]
        stack=[n-1]
        ans=[0]
        for pos in range(n-2,-1,-1):
            while len(stack)>0 and temperatures[stack[-1]]<=temperatures[pos]:
                stack.pop()
            if len(stack)==0:
                ans.append(0)
            else:
                ans.append(stack[-1]-pos)
            stack.append(pos)
        ans.reverse()
        return ans