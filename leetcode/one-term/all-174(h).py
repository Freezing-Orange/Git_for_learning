from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        MAXN = 10**9
        dp = [[MAXN] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]

def test(var):
    s=Solution()
    print(s.calculateMinimumHP(var))

var=[[1,-3,3],[0,-2,0],[-3,-3,-3]]
test(var)