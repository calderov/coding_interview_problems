# Given the inorder and preorder traversals of a binary tree, rebuild the binary tree.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

def printInorder(root):
    if not root:
        return 
    printInorder(root.left)
    print(root.val)
    printInorder(root.right)

if __name__ == "__main__":
    solution = Solution()

    preorder = [1,2,3,4]
    inorder = [2,1,3,4]

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.right = Node(7)
    tree.right.right = Node(4)

    printInorder(tree)
