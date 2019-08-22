# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/22 下午2:36
 @desc:
"""
'''
题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。

解析：
    假设h,i,j是相邻的3的链表结点，初始：a->b->...->h->i->j->...
    假设h前面的结点的指针已经调整完毕，现在我们需要把i的next指针指向h,  a<-b<-...<-h<-i j->...,
    但是这样会导致链表在i和j断裂，所以我们需要把j保存下来
    所以：
        我们在调整结点i的next指针时，除了需要知道结点i本身之外，还需要知道i的前一个结点h,因为我们需要把结点i的next指针指向
        结点h,另外，我们还需要事先保存i的后继结点j,以防止链表断开。因此相应的我们需要定义3个指针，分别指向当前遍历到的结点、
        它的前一个结点、以及后一个结点。
        最后我们试着找到反转链表的头，反转链表的头是原始链表的尾结点。
        
代码鲁棒性：
          ①输入的链表头指针为None
          ②输入的链表只有一个结点
'''


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_chain_table(head):
    if head is None or head.next is None:
        return head

    reverseHead = None
    pNode = head
    prev = None  # 前一个结点

    while pNode is not None:
        pNext = pNode.next
        if pNext is None:
            reverseHead = pNode

        pNode.next = prev
        prev = pNode
        pNode = pNext

    return reverseHead


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

rhead = reverse_chain_table(a)

while rhead:
    print rhead.data
    rhead = rhead.next