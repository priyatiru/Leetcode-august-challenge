'''
Binary search approach
'''

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        lo, hi = 0, candies
        K = 0
        while lo <= hi:
            k = (lo + hi)//2
            if k*(num_people*(num_people+1))//2 + (k*(k-1))//2 * num_people**2 <= candies:
                K = k
                lo = k + 1
            else:
                hi = k - 1
        ans = [(i+1)*K+num_people*(K*(K-1))//2 for i in range(num_people)]
        candies -= sum(ans)
        for i in range(num_people):
            add = min(candies, K * num_people + i + 1)
            ans[i] += add
            candies -= add
            if candies == 0:
                break
        return ans