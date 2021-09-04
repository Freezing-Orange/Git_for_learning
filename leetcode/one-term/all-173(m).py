# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    def __init__(self, root):
        self.nodeStack=[]
        while root:
            self.nodeStack.append(root)
            root=root.left
    
    def next(self) -> int:
        resNode=self.nodeStack.pop()
        tempNode=resNode
        if tempNode.right!=None:
            tempNode=tempNode.right
            while tempNode:
                self.nodeStack.append(tempNode)
                tempNode=tempNode.left
        return resNode.val

    def hasNext(self) -> bool:
        return len(self.nodeStack)>0

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
 
    return level(0)


def testFunc(commandList:List,commandValue:List):
    if len(commandList)!=len(commandValue):
        print("指令数组长度不同")
        return 
    if commandList[0]!="BSTIterator":
        print("未初始化对象")
        return
    root=list_to_binarytree(commandValue[0][0])
    obj=BSTIterator(root)
    for i in range(1,len(commandList)):
        if commandList[i]=="next":
            print(obj.next())
        else:
            print(obj.hasNext())

cL=["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
cV=[[[7,3,15,None,None,9,20]],[],[],[],[],[],[],[],[],[]]
testFunc(cL,cV)
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()