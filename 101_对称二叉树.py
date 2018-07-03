# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
        	return True
        else:
        	return self.ii(root.left,root.right)
    
    def ii(self,a,b):
    	if a == None and b == None:
            return True
        if a and b and a.val == b.val:
            return self.ii(a.left,b.right) and self.ii(a.right,b.left)
        else:
            return False