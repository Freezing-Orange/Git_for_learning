from typing import List
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        def reverse(s,start,end):
            i,j=start,end
            while i<j:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        start,end=0,-1
        for i in range(len(s)):
            if i==len(s)-1:
                reverse(s,start,len(s)-1)
            elif s[i]!=" ":
                end+=1
            else:
                reverse(s,start,end)
                start=i+1
                end=i
        return reverse(s,0,len(s)-1)

def test(valList):
    s=Solution()
    for i in valList:
        s.reverseWords(i)
        print(i)

valList=[
    ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"],
["a"]
]
test(valList)