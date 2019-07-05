# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    
    def getNum(self, l):
        n, i = 0, 0
        while l != None:
            n += l.val * 10 ** i
            i += 1
            l = l.next
        return n
    
    def getList(self, n):
        l = ListNode(n % 10)
        n = n // 10
        p = l
        while n != 0:
            c = ListNode(n % 10)
            p.next = c
            p = c
            n = n // 10
        return l
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.getNum(l1)
        n2 = self.getNum(l2)
        s = n1 + n2
        return self.getList(s)