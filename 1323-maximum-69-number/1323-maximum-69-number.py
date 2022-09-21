class Solution:
    def maximum69Number (self, num: int) -> int:
        digits=[]
        for i in str(num):
            digits.append(int(i))
        #print(digits)
        for x in range(len(digits)):
            if digits[x]==6:
                digits[x]=9
                break
        return int(''.join(str(i) for i in digits))