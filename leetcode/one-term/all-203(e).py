# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):
        if not head:
            return None
        temp=ListNode(next=head)
        preRes=temp
        while temp.next:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return preRes.next

def listToListNode(nums):
    preRes=ListNode()
    preNow=preRes
    for i in nums:
        temp=ListNode(val=i)
        preNow.next=temp
        preNow=preNow.next
    return preRes.next

def showListNode(listNodes):
    temp=listNodes
    if temp:
        print("["+str(temp.val),end="")
        temp=temp.next
    else:
        print("[]")
        return
    while temp:
        print(","+str(temp.val),end="")
        temp=temp.next
    print("]")


def test(val):
    s=Solution()
    i=0
    while i<len(val):
        showListNode(s.removeElements(listToListNode(val[i]),val[i+1]))
        i+=2

val=[
    [1,2,6,3,4,5,6],
6,
[],
1,
[7,7,7,7],
7
]

test(val)