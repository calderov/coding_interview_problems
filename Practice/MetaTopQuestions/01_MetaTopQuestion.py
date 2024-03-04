# 314. Binary Tree Vertical Order Traversal (Medium)
# Given the root of a binary tree, return the vertical order traversal of its
# nodes' values. (i.e., from top to bottom, column by column).
# 
# If two nodes are in the same row and column, the order should be from left
# to right.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def VerticalOrderV1(self, root):
        if not root:
            return []

        columns = {root: 0}
        groupedColumns = {0: [root.val]}
        pending = [root]

        while pending:
            node = pending.pop(0)

            if node.left:
                pending.append(node.left)
                
                column = columns[node] - 1
                columns[node.left] = column
                if column not in groupedColumns:
                    groupedColumns[column] = []
                groupedColumns[column].append(node.left.val)

            if node.right:
                pending.append(node.right)
                
                column = columns[node] + 1
                columns[node.right] = column
                if column not in groupedColumns:
                    groupedColumns[column] = []
                groupedColumns[column].append(node.right.val)
            

        result = []
        for column in sorted(groupedColumns.keys()):
            result.append(groupedColumns[column])
        
        return result
    
    def VerticalOrderV2(self, root):
        if not root:
            return []

        groupedColumns = {0: [root.val]}
        pending = [(root, 0)]

        while pending:
            node, column = pending.pop(0)

            if node.left:
                leftColumn = column - 1
                pending.append((node.left, leftColumn))
                
                if leftColumn not in groupedColumns:
                    groupedColumns[leftColumn] = []
                groupedColumns[leftColumn].append(node.left.val)

            if node.right:
                rightColumn = column + 1
                pending.append((node.right, rightColumn))

                if rightColumn not in groupedColumns:
                    groupedColumns[rightColumn] = []
                groupedColumns[rightColumn].append(node.right.val)

        return [groupedColumns[column] for column in sorted(groupedColumns.keys())]

    def PythonListToTree(self, values, index=0):
        if not values:
            return None
        
        if index >= len(values):
            raise Exception('Index out of range')
        
        if values[index] == None:
            return None

        root = TreeNode(values[index])

        leftIndex = 2 * index + 1
        rightIndex = 2 * index + 2

        if leftIndex < len(values):
            root.left = self.PythonListToTree(values, leftIndex)

        if rightIndex < len(values):
            root.right = self.PythonListToTree(values, rightIndex)

        return root
    
    def VerticalOrder(self, root):
        return self.VerticalOrderV2(root)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree = solution.PythonListToTree([3,9,20,None,None,15,7])
    expectedOutput = [[9],[3,15],[20],[7]]
    output = solution.VerticalOrder(tree)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    tree = solution.PythonListToTree([3,9,8,4,0,1,7])
    expectedOutput = [[4],[9],[3,0,1],[8],[7]]
    output = solution.VerticalOrder(tree)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    tree = solution.PythonListToTree([3,9,8,4,0,1,7,None,None,None,2,5])
    expectedOutput = [[4],[9,5],[3,0,1],[8,2],[7]]
    output = solution.VerticalOrder(tree)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()