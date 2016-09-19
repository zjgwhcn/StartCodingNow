#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

    def createList(self,a):
        if a<=0:
            return False
        if a==1:
            return ListNode(1)
        else:
            head = ListNode(1)
            last = head
            for i in range(2,a+1):
                last.next = ListNode(i)
                last = last.next
            return head
'''
class Solution(object):
    def addTwoNumbers(self,l1,l2):
        carry = 0
        head = ListNode(0)
        last = head
        while l1 and l2:
            Sum = l1.val + l2.val + carry
            carry = Sum/10
            last.next = ListNode(Sum%10)
            l1 = l1.next
            l2 = l2.next
            last = last.next

        while l1:
            Sum = l1.val + carry
            carry = Sum/10
            last.next = ListNode(Sum%10)
            l1 = l1.next
            last = last.next

        while l2:
            Sum = l2.val + carry
            carry = Sum/10
            last.next = ListNode(Sum%10)
            l2 = l2.next
            last = last.next

        if carry > 0:
            last.next = ListNode(carry)

        return head.next

'''
def main():
    a1 = ListNode(8)
    a1.createList(3) 
    a2 = ListNode(6)
    a2.createList(3)
    
    num = Solution()
    num.addTwoNumbers(a1,a2)
    print num

if __name__ == "__main__":main()
'''
