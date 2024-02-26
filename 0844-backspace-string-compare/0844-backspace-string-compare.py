class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        for i in range(len(s)):
            if s[i]=="#":
                if s1:
                    s1.pop()
            else:
                s1.append(s[i])
        
        s2=[]
        for i in range(len(t)):
            if t[i]=="#":
                if s2:
                    s2.pop()
            else:
                s2.append(t[i])

        a="".join(i for i in s1)
        b="".join(j for j in s2)
        return a==b
        
                