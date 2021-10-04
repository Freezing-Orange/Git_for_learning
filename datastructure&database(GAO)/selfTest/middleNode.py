class node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None
def middleNode(head):
    if not head:
        return None
    fast=head
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow