# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        # print(root.val)
        if root == None:
            return None

        # check if swap, then swap
        # if root.left != None and root.right != None:
        temp = root.left
        root.left = root.right
        root.right = temp




        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# g=TreeNode(9,None,None)
# f=TreeNode(6,None,None)
# e=TreeNode(3,None,None)
# d=TreeNode(1,None,None)

# c=TreeNode(7,f,g)
# b=TreeNode(2,d,e)

# a=TreeNode(4,b,c)


# g=TreeNode(9,None,None)
# f=TreeNode(6,None,None)
# e=TreeNode(3,None,None)
# d=TreeNode(1,None,None)

# c=TreeNode(7,f,g)
b = TreeNode(2, None, None)

a = TreeNode(1, b, None)


sol = Solution()
print(sol.invertTree(a).val)
