# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/22 上午7:57
 @desc:
"""
'''
题目：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该结点。
解析：
    在单向链表中删除一个结点，最常见的做法是从头指针开始，顺序遍历查找到要删除的结点，将待删除结点的前一个结点的next指针
指向待删除结点的next结点，然后删除结点即可。但是这个方法的时间复杂度是O(n)。
    现在再重新看一遍题目：给了头指针，还有一个结点指针，所以我们不需要从头遍历才能找到待删除结点，我们已经知道待删除结点了，
但是按照常规的删除方法，我们还需要获得前驱结点。
    所以我们换一种删除的思路：将待删除结点A的后继结点B的值赋给待删除结点A，然后将待删除结点A的next指向其后继结点B的后继结点C，然后
将之前的后继结点B删除即可。这样就可以在O(1)时间内完成链表节点的删除。

另外： 还需考虑的特殊情况：
    ①待删除的链表结点是最后一个结点时，它没有后继结点，只能使用传统的删除结点的方法，从头遍历
    ②如果链表只有一个结点，待删除结点就是该结点
    
'''


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        self.data = None
        self.next = None


def delete_node(head, to_delete):
    if head is None or to_delete is None:
        return
    if head.next is None and head == to_delete:
        to_delete.__del__()
    elif to_delete.next is None:
        p = head
        while p.next != to_delete:
            p = p.next
        p.next = to_delete.next
        to_delete.__del__()
    else:
        to_delete_next = to_delete.next
        to_delete.data = to_delete_next.data
        to_delete.next = to_delete_next.next
        to_delete_next.__del__()


a = ListNode(3)
b = ListNode(2)
c = ListNode(56)
d = ListNode(13)
e = ListNode(7)
a.next = b
b.next = c
c.next = d
d.next = e

head = a
print "before................"
while head:
    print head.data
    head = head.next

delete_node(a, b)
print "after................"
while a:
    print a.data
    a = a.next
