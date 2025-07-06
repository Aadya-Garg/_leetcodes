# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if (not root):
            return 0
        good = 1
        stack = [[root, root.val]]
        while stack:
            node, l = stack.pop()
            l1 = l
            l2 = l
            if node:
                left = node.left
                right = node.right
                if left and left.val >= l:
                    good += 1
                    l1 = left.val
                if right and right.val >= l:
                    good += 1
                    l2 = right.val

                stack.extend([[right,l2], [left, l1]])
        return good