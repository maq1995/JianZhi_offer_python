# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/22 上午10:52
 @desc:
"""
'''
题目1：求链表的中间结点。如果链表中结点总数为奇数，就返回中间结点，如果链表中结点总数为偶数，就返回中间两个结点的任意一个。

解析：
代码功能：
     为了只用一次遍历就找到链表的中间结点，使用两个指针，初始时均指向链表头部，两个指针同时出发，第一个指针一次走一步，第二个
     指针一次走两步，当第二个指针走到链表末尾时，第一个指针指向的就正好是链表的中间结点。
代码鲁棒性:
        ①链表为空
        ②链表长度为1
        ③链表长度为2
        
'''
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def findMiddleNode(head):
    if head is None:
        return

    slow = head
    fast = head

    fast = fast.next if fast.next else None  # 链表长度为1

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
# f = ListNode(6)
# g = ListNode(7)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# f.next = g
#
# print findMiddleNode(a).data


'''
题目2：判断一个单向链表是否形成了环形结构。

解析：
代码功能：
        和找中间结点的题目一样，定义两个指针，同时从链表的头结点出发，一个步长为1，另一个步长为2.如果走得快的指针赶上了慢指针，
        那么说明链表就是环形链表，如果慢指针都走到链表末尾，快指针还没有赶上慢指针，那么就不是环形链表
'''


def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
# f = ListNode(6)
# g = ListNode(7)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# f.next = g
# g.next = c
#
# print has_cycle(a)

'''
题目3： 上面的题目是判断链表中是否有环，进而我们需要判断环的入口在哪里？

解析：
    如果链表存在环，那么两个指针一定会在环内部相遇，此时只需把一个指针重新指向链表头部，另一个不变，
    这次两个指针一次走一步，相遇的地方就是环的入口
'''

def cycle_begining(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = c

print cycle_begining(a).data

'''
总结：当我们用一个指针遍历链表不能解决问题的时候，可以尝试用两个指针来遍历链表，可以让其中一个指针遍历的速度快一些（比如一次
     在链表上走两步），或者让它先在链表上走若干步。
'''
