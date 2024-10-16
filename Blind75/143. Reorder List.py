# TODO: INCORRECT ANSWER! HINT: USE FAST AND SLOW POINTER TO REVERSE TO RIGHT HALF PART OF LIST ONLY
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
        # reverse list
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # prev 為 reversed head
        # dummy node
        dummy = node = ListNode()
        isHead = True
        while node.val != prev.val and node.val != head.val:
            if isHead:
                node.next = head
                head = head.next
            else:
                node.next = prev
                prev = prev.next
            isHead = not isHead
            node = node.next
        


items = [2, 4, 6, 8]
start = node = ListNode(items[0])
for i in range(1, len(items)):
    node.next = ListNode(items[i])    
    node = node.next

sol = Solution()
sol.reorderList(start)
