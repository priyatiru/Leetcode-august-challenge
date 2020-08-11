class Solution:
    def hIndex(self, citations: List[int]) -> int:
        x = len(citations)
        if x == 0:
            return 0
        sortlist = sorted(citations, reverse = True)
        i = 0
        while i<x and sortlist[i] >= (i+1):
            i += 1
        return i