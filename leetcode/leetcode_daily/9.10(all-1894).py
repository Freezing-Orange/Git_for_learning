from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tempSum=0
        sumList=[]
        for i in range(len(chalk)):
            tempSum+=chalk[i]
            if k<tempSum:
                return i
            sumList.append(tempSum)
        k%=tempSum
        i,j=0,len(sumList)-1
        while i<j:
            tempIndex=i+(j-i)//2
            if sumList[tempIndex]==k:
                return tempIndex+1
            elif sumList[tempIndex]>k:
                j=tempIndex
            else:
                i=tempIndex+1
        return j

def test(val):
    i=0
    s=Solution()
    while i<len(val):
        print(s.chalkReplacer(val[i],val[i+1]))
        i+=2

val=[
    [5,1,5],
22,
[3,4,1,2],
25,
[18946,1346,192,2932,1914,968],
19846548
]

test(val)