from typing import List, TypeVar
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(nums,i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        rev(nums,0,len(nums)-1)
        k=k%(len(nums))
        rev(nums,0,k-1)
        rev(nums,k,len(nums)-1)

def test(val):
    s=Solution()
    i=0
    while i<len(val):
        testList=val[i]
        testk=val[i+1]
        s.rotate(testList,testk)
        print(testList)
        i+=2

val=[
    [1,2,3,4,5,6,7],
3,
[-1,-100,3,99],
2
]

test(val)