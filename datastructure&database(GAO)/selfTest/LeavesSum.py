class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    
def LeavesSum(r):
    if r==None:
        return 0
    return r.val+LeavesSum(r.left)+LeavesSum(r.right)