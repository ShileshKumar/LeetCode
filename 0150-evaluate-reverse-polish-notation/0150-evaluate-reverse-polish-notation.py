class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in ['+','-','*','/']:
                num1,num2=stack.pop(),stack.pop()
                if i=='+':
                    stack.append(num2+num1)
                if i=='-':
                    stack.append(num2-num1)
                if i=='*':
                    stack.append(num2*num1)
                if i=='/':
                    stack.append(int(num2/num1))
            else:
                stack.append(int(i))
        return stack.pop()