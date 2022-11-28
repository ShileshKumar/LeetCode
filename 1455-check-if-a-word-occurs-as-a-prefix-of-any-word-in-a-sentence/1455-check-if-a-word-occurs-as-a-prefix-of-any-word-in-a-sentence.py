class Solution:
    def isPrefixOfWord(self, sentence: str, pref: str) -> int:
        cnt=1
        words=sentence.split(" ")
        print(words)
        r=[]
        for i in words:
            if pref in i and i.index(pref)==0:
                r.append(cnt)
            cnt+=1
        
        if len(r)>0:
            return min(r)
        else:
            return -1