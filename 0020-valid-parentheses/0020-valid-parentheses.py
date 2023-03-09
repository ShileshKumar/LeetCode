class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n%2!=0:
            return False
        
        stack=[]
        for i in s:
            if i=='[' or i=='(' or i=='{':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                
                if i==']' and stack[-1]!='[':
                    return False
                
                elif i=='}' and stack[-1]!='{':
                    return False
                
                elif i==')' and stack[-1]!='(':
                    return False
            
                else:
                    stack.pop()
        
        if len(stack)!=0:
            return False
        else:
            return True