from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def countNodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if root.left is None and root.right is None:
        return 1
    count = 0
    if root.left:
        count += countNodes(root.left)
    if root.right:
        count += countNodes(root.right)
    
    return count + 1


def getLeftChild(index):
    return index * 2 + 1
def getRightChild(index):
    return index * 2 + 2

def makeTree(arr,i):
    node = TreeNode(arr[i])

    left_child_index = getLeftChild(i)
    right_child_index = getRightChild(i)

    if left_child_index < len(arr):
        node.left = makeTree(arr,left_child_index)
    if right_child_index < len(arr):
        node.right = makeTree(arr, right_child_index)

    return node

root = makeTree([1,2,3,4,5,6],0)
print(countNodes(root))
