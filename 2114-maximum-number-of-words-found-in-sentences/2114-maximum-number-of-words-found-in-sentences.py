class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l=[]
        for i in sentences:
            l.append(len(i.split(" ")))
        return max(l)