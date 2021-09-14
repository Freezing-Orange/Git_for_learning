class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left<right:
            right&=(right-1)
        return right

def test(val):
    s=Solution()
    i=0
    while i<len(val):
        print(s.rangeBitwiseAnd(val[i],val[i+1]))
        i+=2

val=[
    5,
7,
0,
0,
1,
2147483647,
665659426,
819165164
]

test(val)