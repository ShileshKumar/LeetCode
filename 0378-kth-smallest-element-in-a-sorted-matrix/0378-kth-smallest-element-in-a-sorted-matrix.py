class Solution(object):
    def kthSmallest(self, matrix, k):
        l = []
        for row in matrix:
            l += row
        return sorted(l)[k-1] 