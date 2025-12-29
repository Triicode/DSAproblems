# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        cur = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                cur = cur.next
                list2 = list2.next

        while list1 is not None:
            cur.next = ListNode(list1.val)
            cur = cur.next
            list1 = list1.next

        while list2 is not None:
            cur.next = ListNode(list2.val)
            cur = cur.next
            list2 = list2.next

        return dummy.next