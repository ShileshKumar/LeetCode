class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic={}
        s=s.split(' ')
        if len(pattern)!=len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dic.keys():
                if dic[pattern[i]]==s[i]:
                    continue
                else:
                    return False
            else:
                if s[i] in dic.values():
                    return False
                else:
                    dic[pattern[i]]=s[i]
        return True