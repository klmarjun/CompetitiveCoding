# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = []
        current = l1
        while current:
            val = current.val
            lst1.append(val)
            current = current.next
        lst2 = []
        current = l2
        while current:
            val = current.val
            lst2.append(val)
            current = current.next
        result = []
        carry = 0
        i, j = 0, 0

        while i < len(lst1) or j < len(lst2) or carry:
            x = lst1[i] if i < len(lst1) else 0
            y = lst2[j] if j < len(lst2) else 0
            sum_val = x + y + carry
            carry = sum_val // 10
            result.append(sum_val % 10)
            i += 1
            j += 1

        print(result)
        dummy = ListNode(0)
        current = dummy
        for dig in result:
            current.next = ListNode(int(dig))
            current = current.next
        return dummy.next