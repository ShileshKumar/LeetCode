class Solution(object):
    def isPalindrome(self, s):
        st = "".join(i.lower() for i in s if i.isalnum()) 
        return st==st[::-1]