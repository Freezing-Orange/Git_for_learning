# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        temp,pretemp=head,None
        while temp.next:
            tempnext=temp.next
            temp.next=pretemp
            pretemp,temp=temp,tempnext
        temp.next=pretemp
        return temp

def listToLinkList(vals):
    if not vals:
        return None
    res=ListNode(vals[0])
    temp=res
    for i in range(1,len(vals)):
        nowNode=ListNode(vals[i])
        temp.next=nowNode
        temp=temp.next
    return res

def showListNode(head):
    if not head:
        print("no chain")
        return
    temp=head
    print(temp.val,end=" ")
    temp=temp.next
    while temp:
        print("-> "+str(temp.val),end=" ")
        temp=temp.next
    print()
def test(val):
    s=Solution()
    for i in val:
        showListNode(s.reverseList(listToLinkList(i)))

val=[
    [1,2,3,4,5],
[1,2],
[]
]

test(val)