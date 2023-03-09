class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = ''
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if strs[0][i] != strs[j][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix
        