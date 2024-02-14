# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        seconf_half = slow.next
        prev = slow.next = None
        
        while seconf_half:
            tmp = seconf_half.next
            seconf_half.next = prev
            prev = seconf_half
            seconf_half = tmp
        
        first_half, seconf_half = head, prev

        while seconf_half:
            temp1, temp2 = first_half.next, seconf_half.next
            first_half.next = seconf_half
            seconf_half.next = temp1
            first_half = temp1
            seconf_half = temp2
        