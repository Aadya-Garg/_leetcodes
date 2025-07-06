# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        max_sum = 0
        slow = head
        fast = head.next
        arr.append(slow.val)
        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            arr.append(slow.val)
        slow = slow.next
        while (slow):
            sum_ = arr.pop() + slow.val
            max_sum = max(max_sum, sum_)
            slow = slow.next

        return max_sum

        
        
        
        


        