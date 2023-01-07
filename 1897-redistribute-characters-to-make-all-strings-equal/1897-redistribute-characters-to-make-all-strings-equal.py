class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n=len(words)
        d={}
        for i in words:
            for j in i:
                if j not in d:
                    d[j]=0
                d[j]+=1
        for i in d.values():
            if i%n!=0:
                return False
        return True
        