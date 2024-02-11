# Given the root of a binary tree check wether it is a mirror of itself
#
# Example input:
#
#       1
#   2       2
# 3   4   4   3
#
# Expected result: True

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def MirrorCompare(left, right):
    if not left and not right:
        return True

    if not left or not right:
        return False

    if left.value != right.value:
        return False
    
    return MirrorCompare(left.left, right.right) and MirrorCompare(left.right, right.left)

def IsMirror(root):
    return MirrorCompare(root.left, root.right)

if __name__ == "__main__":
    tree = TreeNode(1)
    
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)

    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(4)

    tree.right.right = TreeNode(3)
    tree.right.left = TreeNode(4)

    print(IsMirror(tree))