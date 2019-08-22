# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/22 上午9:51
 @desc:
"""
'''
题目：输入一个（单向）链表，输出该链表的倒数第k个结点。Eileen符合多数人的习惯，本题从1开始计数，即链表的尾结点是倒数第1个结点。
     例如一个链表有6个结点，从头开始它们的值依次是1 2 3 4 5 6.这个链表的倒数第3个结点是值为4的结点。

解析：
    代码功能：
            暴力方法：因为是单向链表，所以为了得到倒数第k个结点，先遍历链表，得到长度n,那么倒数第k个结点就是正数第n-k+1个结点。
                     但是这样需要遍历两次链表
            
            指针方法：可以只遍历一次链表就可以找到倒数第k个结点。
                    定义两个指针，初始时都指向头指针，然后第一个指针向后走k-1步，第二个指针不动；当第一个指针走第k步开始，
                    第二个指针与第一个指针开始同步向后移动，当第一个指针到达链表尾结点时，第二个指针指向的位置就是倒数第k个结点。
                    
    代码的鲁棒性：①应该想到如果链表的长度小于k时，应该怎么处理。
                ②输入的链表头指针为空
                ③输入的k为0，因为k是一个无符号整数，那么在代码中k-1就不是-1了，而是无符号的0xFFFFFFFF,对应的
                  十进制数为4295967295
    
'''
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def FindKthToTail(head, k):
    if head is None:
        print "this Chian Table is NULL"
        return
    if k <= 0:
        print "the input is INVALID"
        return
    p1 = head
    p2 = head
    for i in xrange(k-1):
        if p1.next is not None:  # 避免链表的长度小于k
            p1 = p1.next
        else:
            print "check your input "
            return

    while p1.next is not None:
        p1 = p1.next
        p2 = p2.next

    return p2


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

h = a
print 'before..............'
while h:
    print h.data
    h = h.next

print '--------------'
print FindKthToTail(a, 7).data