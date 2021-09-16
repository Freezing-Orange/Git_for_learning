from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursesCount=[0]*numCourses
        count=0
        for courseCP in prerequisites:
            coursesCount[courseCP[0]]+=1
            count+=1
        canCoureses=[]
        for i in range(numCourses):
            if coursesCount[i]==0:
                canCoureses.append(i)
        while canCoureses:
            newCanCoureses=[]
            i=0
            while i<len(prerequisites):
                if prerequisites[i][1] in canCoureses:
                    coursesCount[prerequisites[i][0]]-=1
                    if coursesCount[prerequisites[i][0]]==0:
                        newCanCoureses.append(prerequisites[i][0])
                    count-=1
                    del prerequisites[i]
                else:
                    i+=1
            canCoureses=newCanCoureses
        if count==0:
            return True
        return False

def test(val):
    s=Solution()
    i=0
    while i<len(val):
        print(s.canFinish(val[i],val[i+1]))
        i+=2
val=[
    2,
[[1,0]],
2,
[[1,0],[0,1]],
9999,
[[5161,165],[165,9189],[165,131],[159,1918],[9189,5161]],
2,
[[0,0]]
]

test(val)