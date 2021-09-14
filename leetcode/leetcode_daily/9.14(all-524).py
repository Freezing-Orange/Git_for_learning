from typing import List
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x),x))
        for word in dictionary:
            i,length=0,len(word)
            for letter in s:
                if letter==word[i]:
                    i+=1
                    if i==length:
                        return word
        return ""

def test(val):
    s=Solution()
    i=0
    while i<len(val):
        print(s.findLongestWord(val[i],val[i+1]))
        i+=2

val=[
    "abpcplea",
["ale","apple","monkey","plea"],
"abpcplea",
["a","b","c"],
]

test(val)
