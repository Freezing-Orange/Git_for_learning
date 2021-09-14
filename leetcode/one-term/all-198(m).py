from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        maxPrevious=nums[0]
        maxNow=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            maxPrevious, maxNow=maxNow, max(maxPrevious+nums[i], maxNow)
        return max(maxPrevious,maxNow)

def test(val):
    s=Solution()
    for i in val:
        print(s.rob(i))

val=[
    [1,2,3,1],
[2,7,9,3,1],
[125],
[2,1,1,2]
]

test(val)