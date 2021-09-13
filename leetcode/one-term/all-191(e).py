class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+=1
            n&=n-1
        return res

def test(val):
    s=Solution()
    for i in val:
        print(s.hammingWeight(i))

val=[
0x00000000000000000000000000001011,
0x00000000000000000000000010000000,
0x11111111111111111111111111111101,
]

test(val)