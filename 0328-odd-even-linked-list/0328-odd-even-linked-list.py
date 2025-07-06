# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node = head
        prev = None
        to_add = None
        add_pointer = None
        while (node and node.next):
            prev = node
            node = node.next
            
            if (to_add):
                add_pointer.next = node
                prev.next = node.next
                node = node.next
                add_pointer.next.next = None
                add_pointer = add_pointer.next
            else:
                to_add = node
                prev.next = node.next
                node = node.next
                to_add.next = None
                add_pointer = to_add

        if (node):
            node.next = to_add
        elif (prev):
            prev.next = to_add
        else:
            return None
        return head
            