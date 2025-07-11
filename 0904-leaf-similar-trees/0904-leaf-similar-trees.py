# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack1 = [root1]
        l1 = []
        stack2 = [root2]

        while stack1:
            node = stack1.pop()
            if node:
                left = node.left
                right = node.right
                if (not left and not right):
                    l1.append(node)
                stack1.extend([right,left])
        print(l1)
        ind = 0
        length = len(l1)
        leaves2 = 0
        while stack2:
            node = stack2.pop()
            if node:
                left = node.left
                right = node.right
                if (not left and not right):
                    leaves2 += 1
                    if ind >= length or l1[ind].val != node.val:
                        return False
                    ind += 1
                stack2.extend([right,left])
        if (leaves2 < length):
            return False
        return True

            
        