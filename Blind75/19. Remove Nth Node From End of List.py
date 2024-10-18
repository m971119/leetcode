from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Optimized Solution: O(n)
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = left = ListNode(0, head)
        right = head

        for i in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


"""
My first attempt: O(3n)
"""
class Solution_FirstAttempt:
    def reverseList(self, head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
    def removeNthFromStart(self, head, n):
        curr = head
        prev = None
        for i in range(1, n + 1):
            next = curr.next
            if i == n:
                if prev:
                    prev.next = next
            prev = curr
            curr = next
        return curr if n == 1 else head
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse list
        reversedHead = self.reverseList(head)
        # remove nth from start
        reversedHead = self.removeNthFromStart(reversedHead, n)
        # reverse list again
        return self.reverseList(reversedHead)