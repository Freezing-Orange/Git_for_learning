from random import randint

def rand7():
    return randint(1,7)

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a=rand7()
        b=rand7()
        while a>4 and b<4:
            a=rand7()
            b=rand7()
        return (a+b)%10+1

def test(n):
    # n表示调用了几次rand10
    s=Solution()
    count=[0]*11
    length=0
    for _ in range(n):
        val=s.rand10()
        if length==19:
            print("%2s"%str(val))
            length=0
        else:
            print("%2s"%str(val),end=" ")
            length+=1
        count[val]+=1
    if length:
        print('\n')
    for i in range(1,11):
        print(str(i)+"一共有"+str(count[i])+"个")


test(100)