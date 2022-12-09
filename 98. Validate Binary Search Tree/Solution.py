# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        return self.recursiveCheckBST(root, [float('-inf'),float('inf')])

    def recursiveCheckBST(self, root, limits):
        if root == None:
            return True

        # if limits == None:
            # limits = [root.val, root.val]

        if root.val <= limits[0]: #bigger than this
            return False
        if root.val >= limits[1]: #smaller than this
            return False


        leftCheck = self.recursiveCheckBST(root.left, [limits[0],root.val])
        rightCheck = self.recursiveCheckBST(root.right, [root.val,limits[1]])

        if leftCheck and rightCheck:
            return True
        return False


sol = Solution()
root=TreeNode(50,TreeNode(40,TreeNode(30),TreeNode(45)),TreeNode(70,TreeNode(49),TreeNode(80)))
root=TreeNode(50)
root=TreeNode(2,TreeNode(2),TreeNode(2))
print(sol.isValidBST(root))