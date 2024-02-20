# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr1, curr2 = l1, l2
        curr_result = result
        rest = 0

        while curr1 or curr2:
            next_node = ListNode()
            curr_result.next = next_node
            curr_result = curr_result.next
            if curr1 == None:
                s = curr2.val
            elif curr2 == None:
                s = curr1.val
            else:
                s = curr1.val + curr2.val

            if s + rest < 10:
                curr_result.val = s + rest
                rest = 0
            else:
                curr_result.val = (s + rest) % 10 
                rest = (s + rest) // 10

            if curr1:
                curr1 = curr1.next
            else:
                curr1 = curr1

            if curr2:
                curr2 = curr2.next
            else:
                curr2 = curr2
        if rest > 0:
            next_extra_node = ListNode(rest)
            curr_result.next = next_extra_node
        
        return result.next
            