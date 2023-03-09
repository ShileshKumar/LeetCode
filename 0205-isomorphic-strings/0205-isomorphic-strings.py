class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                hashmap[s[i]] = t[i]
				
         # For few tricky edge cases      
        if len(set(hashmap.values())) != len(hashmap.values()): 
            return False    
        return True