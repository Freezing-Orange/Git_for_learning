class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findINorderElementAfterV(root,v):
    p=root
    temp=root
    while p:
        if v==p.value:
            return findMin(p.right) or temp
        if v>p.value:
            if v!=p.right.value:
            	p=p.right
            	temp=p.right.value
            else:
                return findMin(p.right)
        else:
            p=p.left
    return None

def findMin(root):
    if not root:
        return None
    p=root
    while p.left:
        p=p.left
    return p.value

def sortedArrayToBST(self, nums):
    def helper(nleft, nright):
        if nleft > nright:
            return None

        # 总是选择中间位置右边的数字作为根节点
        mid = (nleft + nright + 1) // 2

        root = TreeNode(nums[mid])
        root.left = helper(nleft, mid - 1)
        root.right = helper(mid + 1, nright)
        return root

    return helper(0, len(nums) - 1)

    
a=[1,2,3,4,5,6]
