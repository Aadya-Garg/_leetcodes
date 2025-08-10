# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #DFS
        if root is None:
            return True

        vr = root.val
        left_interval_ = []
        right_interval_ = []
        if vr - 1 >= -2**31:
            left_interval_ = [-2**31,vr-1]
        if vr + 1 <= 2**31:
            right_interval_ = [vr+1,2**31]
        stack = [[root, left_interval_, right_interval_]]

        while stack:
            node, left_interval, right_interval = stack.pop()
            v = node.val
            left = node.left
            right = node.right
            if not left and not right:
                continue

            if left and (left_interval == [] or left.val < left_interval[0] or left.val > left_interval[1]):
                return False
            if right and (right_interval == [] or right.val < right_interval[0] or right.val > right_interval[1]):
                return False

            if right:
                l = [right_interval[0], right.val - 1]
                if l[0] > l[1]:
                    l = []
               
                r = [right.val + 1, right_interval[1]]
                if r[0] > r[1]:
                    r = []
                stack.append([right, l, r])
            if left:
                l = [left_interval[0], left.val - 1]
                r = [left.val + 1, left_interval[1]]
                if l[0] > l[1]:
                    l = []
                r = [left.val + 1, left_interval[1]]
                if r[0] > r[1]:
                    r = []
                stack.append([left, l, r])
        return True
