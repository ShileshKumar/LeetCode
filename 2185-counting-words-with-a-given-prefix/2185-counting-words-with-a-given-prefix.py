class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt=0
        for i in words:
            if pref in i and i.index(pref)==0:
                cnt+=1
        return cnt