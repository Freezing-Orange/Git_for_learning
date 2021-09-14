from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res=dict()
        def everylevel(r,l):
            if r:
                res[l]=r.val
                everylevel(r.left,l+1)
                everylevel(r.right,l+1)
        everylevel(root,0)
        return [*res.values()]
