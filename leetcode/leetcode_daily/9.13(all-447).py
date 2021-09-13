from typing import List
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res=0
        for i in range(len(points)):
            distance=dict()
            for j in range(len(points)):
                if i!=j:
                    nowDistance=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                    if nowDistance in distance.keys():
                        n=distance[nowDistance]
                        res+=2*n
                        distance[nowDistance]=n+1
                    else:
                        distance[nowDistance]=1
        return res

def test(val):
    s=Solution()
    for i in val:
        print(s.numberOfBoomerangs(i))

val=[
    [[0,0],[1,0],[2,0]],
[[1,1],[2,2],[3,3]],
[[1,1]]
]

test(val)