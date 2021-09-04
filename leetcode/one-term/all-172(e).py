class Solution:
    def trailingZeroes(self, n: int) -> int:
        res=0
        while n//5>0:
            res+=(n//5)
            n//=5
        return res

s=Solution()
testExample=[3,
5,
0,
5000]
for i in testExample:
    print(s.trailingZeroes(i))