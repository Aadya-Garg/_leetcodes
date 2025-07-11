# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        while (root):
            if (root.val == val):
                return root
            left = root.left
            right = root.right
        
            if (left and left.val == val):
                return left
            elif (right and right.val == val):
                return right
            elif (left and val < left.val):
                root = left.left
            elif(left and val>left.val and val<root.val):
                root = left.right
            elif(right and val<right.val and val > root.val):
                root = right.left
            elif (right):
                root = right.right
            else:
                return None
        
        return None

        