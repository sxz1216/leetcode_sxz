# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        cur_level = [root]
        results = []
        while cur_level:
            cur_res = []
            next_level = []
            for i in cur_level:
                cur_res.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            results.append(cur_res)
            cur_level = next_level
        results.reverse()
        return results