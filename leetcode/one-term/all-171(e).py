class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        digit=1
        for i in range(len(columnTitle)-1,-1,-1):
           res+=(ord(columnTitle[i])-64)*digit
           digit*=26
        return res

s=Solution()
testExample=["A",
"AB",
"ZY",
"FXSHRXW"]
for i in testExample:
    print(s.titleToNumber(i))