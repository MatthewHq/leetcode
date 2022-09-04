# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    output = []

    def zigzagLevelOrder(self, root):
        if root==None:
            return []
        Solution.output=[]
        self.traverse(root, 0)
        # print(self.output)
        # i=1
        # while i <len(self.output):
            
        #     self.output[i].reverse()
        #     i+=2

        return self.output

    def traverse(self, node, level):
        # print(level)
        if len(self.output) <= level:
            self.output.append([])
        self.output[level].append(node.val)
        level += 1
        if node.left!=None:
            self.traverse(node.left, level)
        if node.right!=None:
            self.traverse(node.right, level)
        


sol = Solution()
n4 = TreeNode(15, None, None)
n3 = TreeNode(7, None, None)
n2 = TreeNode(20, n4, n3)

# l1=TreeNode(5, None, None)
# l2=TreeNode(6, l1, None)
# l3=TreeNode(8, l2, None)
# n1 = TreeNode(9, l3, None)
n1 = TreeNode(9, None, None)
# root=TreeNode(1,None,None)
# root=TreeNode(1,None,None)
# root=TreeNode(1,None,None)

root = TreeNode(3, n1, n2)

print(sol.zigzagLevelOrder(root))
