class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)<2:
            return True
        sdict=dict()
        for i in range(len(s)):
            stemp, ttemp=s[i], t[i]
            if stemp in sdict.keys():
                if sdict[stemp]!=ttemp:
                    return False
            elif ttemp not in sdict.values():
                sdict[stemp]=ttemp
            else:
                return False
        return True

def test(val):
    s=Solution()
    i=0
    while i<len(val):
        print(s.isIsomorphic(val[i],val[i+1]))
        i+=2

val=[
    "egg",
"add",
"foo",
"bar",
"paper",
"title"
]

test(val)