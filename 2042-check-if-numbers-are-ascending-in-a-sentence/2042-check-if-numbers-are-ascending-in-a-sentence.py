class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev=float('-inf')
        for i in s.split():
            if i.isdigit():
                if int(i)<=prev:
                    return False
                else:
                    prev=int(i)
        return True
                