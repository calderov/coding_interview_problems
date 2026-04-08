# Find the closest element in Binary Search Tree
# https://www.geeksforgeeks.org/dsa/find-closest-element-binary-search-tree/
#
# Given a binary search tree and a target node K. Find the node with the minimum
# absolute difference with the given target value K.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Time complexity: O(log(n))
# Space complexity: O(log(n))
def findNodeClosestToKRecursive(node, k, closestNode=None):
    if not node:
        return closestNode
    
    if not closestNode or abs(node.val - k) < abs(closestNode.val - k):
        closestNode = node

    if k < node.val:
        return findNodeClosestToKRecursive(node.left, k, closestNode)
    else:
        return findNodeClosestToKRecursive(node.right, k, closestNode)

# Time complexity: O(log(n))
# Space complexity: O(1)
def findNodeClosestToKIterative(root, k):
    node = root
    closestNode = node

    while node:
        if abs(node.val - k) < abs(closestNode.val - k):
            closestNode = node
        
        if k < node.val:
            node = node.left
        else:
            node = node.right

    return closestNode


def findNodeClosestToK(node, k):
    return findNodeClosestToKIterative(node, k)

def listToTree(values, index=0):
    if not values or index < 0 or index >= len(values) or values[index] == None:
        return None
    
    node = Node(values[index])
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2

    node.left = listToTree(values, leftIndex)
    node.right = listToTree(values, rightIndex)

    return node

if __name__=="__main__":
    root = listToTree([9, 4, 17, 3, 6, None, 22, None, None, 5, 7, 20])
    k = 18
    expected = 17
    output = findNodeClosestToK(root, k).val
    print(expected)
    print(output)
    print(expected == output)