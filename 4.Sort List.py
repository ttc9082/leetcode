__author__ = 'TTc9082'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        while fast.next != None:
            fast = fast.next.next
            if fast == None:
                break
            slow = slow.next
        right = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(right)
        return self.merge(l, r)

    def sortList2(self, head):
        length = 0
        count = head
        while count != None:
            count = count.next
            length += 1
        if length > 1:
            left = head
            walker = left
            for i in range(length/2-1):
                walker = walker.next
            right = walker.next
            walker.next = None
            l = self.sortList(left)
            r = self.sortList(right)
            res = self.merge(l, r)
            return res
        else:
            return head

    def merge(self, left, right):
        c = res = ListNode(-1)
        while not (left is None or right is None):
            if left.val < right.val:
                c.next = left
                left = left.next
            else:
                c.next = right
                right = right.next
            c = c.next
        c.next = left or right
        res = res.next
        return res