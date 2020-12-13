# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        if fast == None or fast.next == None:
            return False
        fast = fast.next.next
        slow = head
        while (fast != slow):
            if fast == None or fast.next == None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

a = ListNode(1, None)
b = ListNode(1, None)
print(a==b)


