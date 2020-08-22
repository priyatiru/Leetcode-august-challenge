class Solution:
    
    def numPoints(self, rect) -> int:
        x1, y1, x2, y2 = rect
        return (x2 - x1 + 1) * (y2 - y1 + 1)

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.presum = [0]
        for i in range(len(rects)):
            self.presum.append(self.presum[-1] + self.numPoints(rects[i]))

    def pick(self) -> List[int]:
        n =  random.randint(1, self.presum[-1])
        i = bisect.bisect_left(self.presum, n) 
        n -= self.presum[i-1]
        x1, y1, x2, y2 = self.rects[i-1]
        q, r = divmod(n, x2 - x1 + 1)
        if r:
            return [x1 + r -1, y1 + q]
        return [x2, y1 + q -1]
           

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()