# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        res = ListNode(0)
        res.next = head
        cur = head.next
        last = head
        while cur is not None:
            pos = res
            node = res.next
            if cur.val >= last.val:
                last = cur
                cur = cur.next
                continue
            while cur.val > node.val:
                node = node.next
                pos = pos.next
            pos.next = ListNode(cur.val)
            pos.next.next = node
            cur = cur.next
            last.next = cur
        return res.next