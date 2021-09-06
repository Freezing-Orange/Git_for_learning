from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j=0,len(nums)-1
        while i<=j:
            temp=i+(j-i)//2
            if nums[temp]==target:
                return temp
            elif nums[temp]>target:
                j=temp-1
            else:
                i=temp+1
        return -1

def test(valList):
    s=Solution()
    for i in range(0,len(valList),2):
        print(s.search(valList[i],valList[i+1]))

valList=[
    [-1,0,3,5,9,12],
9,
[-1,0,3,5,9,12],
2,
[2,5],
5,
[5],
5,
[5],
-1,
]
test(valList)