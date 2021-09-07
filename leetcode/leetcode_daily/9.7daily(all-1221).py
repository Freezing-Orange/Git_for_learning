class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lcount=0
        rcount=0
        res=0
        for i in s:
            if i=="R":
                rcount+=1
                if rcount==lcount:
                    res+=1
            else:
                lcount+=1
                if rcount==lcount:
                    res+=1
        return res

def test(val):
    s=Solution()
    for i in val:
        print(s.balancedStringSplit(i))

val=[
    "RLRRLLRLRL",
"RLLLLRRRLR",
"LLLLRRRR",
"RLRRRLLRLL"
]
test(val)