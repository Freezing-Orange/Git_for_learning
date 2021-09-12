class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        leftMax=0
        leftMin=0
        for i in s:
            if i=="(":
                leftMin+=1
                leftMax+=1
            elif i=="*":
                leftMax+=1
                if leftMin>0:
                    leftMin-=1
            else:
                if leftMin>0:
                    leftMin-=1
                leftMax-=1
                if leftMax<0:
                    return False
        if leftMin==0:
            return True
        else:
            return False

def test(val):
    s=Solution()
    for i in val:
        print(s.checkValidString(i))

val=[
    "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()",
    "()",
"(*)",
"(*))",
")",
"(*)))"
]

test(val)