# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        cur_level = [root]
        result = 1
        while cur_level:
            cur_res = 0
            next_level = []
            for i in cur_level:
                if i.left == None and i.right == None:
                    return result
                if i.left != None:
                    next_level.append(i.left)
                if i.right != None:
                    next_level.append(i.right)
            result += 1
            cur_level = next_level