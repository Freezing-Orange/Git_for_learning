import functools
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a,b):
            if a+b>b+a:
                return 1
            elif a+b==b+a:
                return 0
            else:
                return -1
        numsMap=map(str,nums)
        res=sorted(numsMap,key=functools. cmp_to_key(cmp),reverse=True)
        return "".join(res) if res[0]!="0" else "0"

def test(var:List):
    s=Solution()
    for i in var:
        print(s.largestNumber(i))

var=[
    [10,2],
[3,30,34,5,9],
[1],
[10]
]

test(var)