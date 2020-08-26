class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [("Fizz"*(n%3==0)+"Buzz"*(n%5==0)) or str(n) for n in range(1,n+1)]
        