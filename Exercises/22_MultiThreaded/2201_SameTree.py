# Problem:
# Given the roots of two binary trees 'p' and 'q', write a function to check
# if they are the same or not.
# 
# Two binary trees are considered the same if they met following two
# conditions:
# 
#   1. Both tree are structurally identical.
# 
#   2. Each corresponding node on both the trees have the same value.
# 
# Example:
#
#   Given the following binary trees
#
#           ┌──┐                 ┌──┐
#        ┌──┤10├──┐           ┌──┤10├──┐
#        │  └──┘  │           │  └──┘  │
#        │        │           │        │
#        │        │           │        │
#        ▼        ▼           ▼        ▼
#       ┌──┐    ┌──┐         ┌──┐     ┌──┐
#    ┌──┤ 4│  ┌─┤15│     ┌───┤ 4│   ┌─┤15│
#    │  └──┘  │ └──┘     │   └──┘   │ └──┘
#    │        │          │          │
#    │        │          │          │
#    ▼        ▼          ▼          ▼
#   ┌──┐     ┌──┐       ┌──┐       ┌──┐
#   │ 1│     │14│       │ 1│       │14│
#   └──┘     └──┘       └──┘       └──┘
#
#   The expected output is TRUE, as both threes are structurally the same and
#   the values at their isomorphic nodes are the same.

import os
import threading

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.isSame = True # Used for multi threaded approach

    # Single threaded solution:
    # Traverse both trees T1 and T2 from their respective roots using recursive DFS. At each level of recursion, compare the
    # root of each of the subtrees and do the following 
    # 
    # 1. If both roots are null, return True.
    # 2. If one root is null but the other isn't, return False.
    # 3. If none of the roots is null but they differ in value, return False.
    # 4. If none of the roots is null and their value is the same, return the result of recursively calling
    #    this same DFS function on the left and right subtrees of both roots.
    # 
    # Solution complexity:
    # Time complexity: O(min(N, M)) where N is the number of nodes on the first tree and M is the number of nodes on the second one.
    # Space complexity: O(min(N, M))
    def IsSameTreeSingleThread(self, tree1, tree2):
        if not tree1 and not tree2:
            return True

        if not tree1 or not tree2:
            return False

        if tree1.val != tree2.val:
            return False
        
        return self.IsSameTreeSingleThread(tree1.left, tree2.left) and self.IsSameTreeSingleThread(tree1.right, tree2.right)


    # Multi threaded solution:
    # Set a class scoped variable named isSame and have it initialized to True. This will help us track if both
    # trees are equal.
    #
    # Traverse both trees T1 and T2 from their respective roots using recursive DFS. At each level of recursion, compare the
    # root of each of the subtrees and do the following:
    # 
    # 1. If both roots are null, return True.
    # 2. If one root is null but the other isn't, return False.
    # 3. If none of the roots is null but they differ in value, return False.
    # 4. If none of the roots is null and their value is the same, return the result of joining the current value of 
    #    isSame and the result of recursively calling this same DFS function on the left and right subtrees for both roots, 
    #    speed up this step by spawning a new thread to explore the right subtree, and use the current thread to explore the left subtree.
    #    Remember to keep track of the available threads, and await for them to finish before returning the final value of isSame.
    # 
    # Solution complexity:
    # Time complexity: O(min(N, M)) where N is the number of nodes on the first tree and M is the number of nodes on the second one.
    # Space complexity: O(min(N, M))
    def IsSameTreeMultiThread(self, tree1, tree2, numThreads):
        if not tree1 and not tree2:
            return True
        
        if not tree1 or not tree2:
            return False
        
        if tree1.val != tree2.val:
            return False
        
        # If we can spawn new threads, use a new one to check the right branch
        # and use the current thread to check the left branch
        if numThreads > 0:
            # Spawn a new thread to check the right subtree
            def checkRight():
                nonlocal tree1
                nonlocal tree2
                nonlocal numThreads
                self.isSame = self.isSame and self.IsSameTreeMultiThread(tree1.right, tree2.right, numThreads // 2)
            
            t1 = threading.Thread(target=checkRight)
            t1.start()

            # Use the current thread to check the left subtree
            self.isSame = self.isSame and self.IsSameTreeMultiThread(tree1.left, tree2.left, numThreads // 2)

            # Wait for the right thread to finish
            t1.join()
        
        # Otherwise, fallback to a single thread approach
        else:
            self.isSame = self.isSame and self.IsSameTreeMultiThread(tree1.right, tree2.right, 0) and self.IsSameTreeMultiThread(tree1.left, tree2.left, 0)

        return self.isSame

    def IsSameTree(self, tree1, tree2):
        self.isSame = True
        numThreads = os.cpu_count()
        return self.IsSameTreeMultiThread(tree1, tree2, numThreads)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree1 = TreeNode(10)
    tree1.left = TreeNode(4)
    tree1.right = TreeNode(15)
    tree1.left.left = TreeNode(1)
    tree1.right.left = TreeNode(14)

    tree2 = TreeNode(10)
    tree2.left = TreeNode(4)
    tree2.right = TreeNode(15)
    tree2.left.left = TreeNode(1)
    tree2.right.left = TreeNode(14)

    expectedSolution = True
    output = solution.IsSameTree(tree1, tree2)
    print(output, expectedSolution, output == expectedSolution)

    # Example 2
    tree1 = TreeNode(10)
    tree1.left = TreeNode(4)
    tree1.right = TreeNode(15)
    tree1.left.left = TreeNode(1)
    tree1.right.left = TreeNode(14)

    tree2 = TreeNode(10)
    tree2.left = TreeNode(4)
    tree2.right = TreeNode(15)
    tree2.left.left = TreeNode(1)
    tree2.right.left = TreeNode(14)
    tree2.right.right = TreeNode(20) # Extra node

    expectedSolution = False
    output = solution.IsSameTree(tree1, tree2)
    print(output, expectedSolution, output == expectedSolution)

    # Example 3
    tree1 = TreeNode(10)
    tree1.left = TreeNode(4)
    tree1.right = TreeNode(15)
    tree1.left.left = TreeNode(1)
    tree1.right.left = TreeNode(14)

    tree2 = TreeNode(10)
    tree2.left = TreeNode(9) # Different value
    tree2.right = TreeNode(15)
    tree2.left.left = TreeNode(1)
    tree2.right.left = TreeNode(14)

    expectedSolution = False
    output = solution.IsSameTree(tree1, tree2)
    print(output, expectedSolution, output == expectedSolution)