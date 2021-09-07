from typing import List
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res=0
        kingX=king[0]
        kingY=king[1]
        def judgeDir(queens,kingX,kingY,dirX,dirY):
            tempX=kingX+dirX
            tempY=kingY+dirY
            while 8>tempX>=0 and 0<=tempY<8:
                if [tempX,tempY] in queens:
                    return [[tempX,tempY]]
                else:
                    tempX+=dirX
                    tempY+=dirY
            return []
        return judgeDir(queens,kingX,kingY,0,1)+judgeDir(queens,kingX,kingY,1,1)+\
            judgeDir(queens,kingX,kingY,1,-1)+judgeDir(queens,kingX,kingY,0,-1)+\
                judgeDir(queens,kingX,kingY,1,0)+judgeDir(queens,kingX,kingY,-1,0)+\
                    judgeDir(queens,kingX,kingY,-1,1)+judgeDir(queens,kingX,kingY,-1,-1)

def test(val):
    s=Solution()
    for i in range(0,len(val),2):
        print(s.queensAttacktheKing(val[i],val[i+1]))

val=[
    [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]],
[0,0],
[[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]],
[3,3],
[[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]],
[3,4]
]
test(val)