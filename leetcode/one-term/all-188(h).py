from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def maxiumnProfit(prices:List[int]):
            res=0
            temp=prices[0]
            for i in range(1,len(prices)):
                if prices[i]<=temp:
                    temp=prices[i]
                else:
                    res+=(prices[i]-temp)
                    temp=prices[i]
            return res
        
        days=len(prices)
        if days==0 or k==0:
            return 0
        if k>=days//2:
            return maxiumnProfit(prices)
        dp=[[0,-prices[0]] for _ in range(k+1)]
        for i in range(1,days):
            for j in range(k,0,-1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])
        return dp[k][0]

def test(val):
    s=Solution()
    i=0
    while i<len(val):
        print(s.maxProfit(val[i],val[i+1]))
        i+=2

val=[
    2,
[2,4,1],
2,
[3,2,6,5,0,3],
4,
[15,18,94,84,42,47,45,95,48,61,53,8,4,7,9,2,54,45,96],
]
test(val)