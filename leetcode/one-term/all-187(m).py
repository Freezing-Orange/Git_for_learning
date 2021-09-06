from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        appearSet=set()
        ansSet=set()
        for i in range(len(s)-9):
            if s[i:i+10] not in appearSet:
                appearSet.add(s[i:i+10])
            else:
                ansSet.add(s[i:i+10])
        return list(ansSet)

def test(valList):
    s=Solution()
    for i in valList:
        print(s.findRepeatedDnaSequences(i))

valList=[
    "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
"AAAAAAAAAAAAA"
]
test(valList)