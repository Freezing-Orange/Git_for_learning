class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        while s[i]==" ":
            i-=1
        res=0
        while  i>=0 and s[i]!=" ":
            res+=1
            i-=1
        return res

def test(val):
    s=Solution()
    for i in val:
        print(s.lengthOfLastWord(i))

val=[
    "Hello World",
"   fly me   to   the moon  ",
"luffy is still joyboy",
"a"
]

test(val)