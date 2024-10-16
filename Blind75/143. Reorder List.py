# HINT: USE FAST AND SLOW POINTER TO REVERSE TO RIGHT HALF PART OF LIST ONLY
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def toList(self):
        a = []
        node = self
        while node:
            a.append(node.val)
            node = node.next
        return a

class Solution:
    def reorderList(self, head) -> None:
        # Find middle node by slow fast pointer
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # put the later half into second and reverse list
        # note: slow.next = None trims the later half part off so that head only has the first half part of the original list
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        


items = [2, 4, 6, 8, 10]
start = node = ListNode(items[0])
for i in range(1, len(items)):
    node.next = ListNode(items[i])    
    node = node.next

sol = Solution()
sol.reorderList(start)
print(start.toList())
