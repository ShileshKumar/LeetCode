class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        a=s[:n//2]
        b=s[n//2:]
        #print(a,b)
        vowels='aeiou'
        a1,b1=0,0
        for i in a:
            if i.lower() in vowels:
                a1+=1
        for i in b:
            if i.lower() in vowels:
                b1+=1
        
        return a1==b1