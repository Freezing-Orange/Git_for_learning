class Solution:
    def fib(self, n: int) -> int:
        i,j=0,1
        if n==0:
            return i
        if n==1:
            return j
        for k in range(2,n+1):
            i,j=j,(i+j)%1000000007
        return j


s=Solution()
print(s.fib(0))
print(s.fib(10))
print(s.fib(100))