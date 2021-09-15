class Solution:
    def countPrimes(self, n: int) -> int:
        nums=[1]*n
        count=0
        for i in range(2,n):
            if i*i<n:
                if nums[i]:
                    count+=1
                    j=2
                    while i*j<n:
                        nums[i*j]=0
                        j+=1
            else:
                if nums[i]:
                    count+=1

        return count

def test(val):
    s=Solution()
    for i in val:
        print(s.countPrimes(i))

val=[
    10,
1,
0,
2,
3,
435534
]

test(val)