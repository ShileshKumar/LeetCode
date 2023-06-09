class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters)-1
        while low <= high:
            mid = (low+high)//2
            if ord(letters[mid]) <= ord(target):
                low = mid+1
            else:
                high = mid-1
        if low >= len(letters):
            return letters[0]
        else:
            return letters[low]