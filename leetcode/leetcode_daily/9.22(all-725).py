from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        listLength=0
        temp=head
        while temp:
            temp=temp.next
            listLength+=1
        shortLength=listLength//k
        longerNums=listLength%k
        nowPart=0
        res=[]
        nowNode=head
        while nowPart<k:
            thisLength=0
            thisList=nowNode
            while nowNode:
                thisLength+=1
                if (thisLength==shortLength+1 and nowPart<longerNums) or (thisLength==shortLength and nowPart>=longerNums):
                    temp=nowNode.next
                    nowNode.next=None
                    nowNode=temp
                    break
                else:
                    nowNode=nowNode.next       
            res.append(thisList)
            nowPart+=1
        return res


