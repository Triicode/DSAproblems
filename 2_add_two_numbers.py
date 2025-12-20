# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 is not None or l2 is not None or carry!=0:
            if l1 is not None:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
            if l2 is not None:
                y = l2.val
                l2=l2.next
            else:
                y = 0
            cur.next = ListNode((x+y+carry)%10)
            cur = cur.next
            carry = (x+y+carry)//10
        return dummy.next