# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/22 下午3:01
 @desc:
"""
'''
题目：输入两个递增排序的链表，合并这两个链表并使得新链表中的结点仍然是按照递增排序的。

解析：
    每个链表使用一个指针，进行比较，可以使用递归也可以使用循环
    
代码的鲁棒性：
           ①其中一个链表是空的
'''


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# 递归版本
def merge_chain_tables(head1, head2):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1
    pMergedHead = None
    if head1.data <= head2.data:
        pMergedHead = head1
        pMergedHead.next = merge_chain_tables(head1.next, head2)
    else:
        pMergedHead = head2
        pMergedHead.next = merge_chain_tables(head1, head2.next)

    return pMergedHead


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(9)
a.next = c
# c.next = e

b.next = d
# d.next = f
# f.next = g

mhead = merge_chain_tables(a, b)
while mhead:
    print mhead.data
    mhead = mhead.next
