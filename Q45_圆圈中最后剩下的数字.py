# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/18 上午10:21
 @desc:
"""
'''
题目：0,1,...,n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
     例如0,1,2,3,4这五个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前四个数字依次是：2,0,4,1，最后剩下的数字是3.
'''

'''
解法1：用环形链表模拟圆圈
    
'''


class ListNode:
    def __init__(self, data):
        self.data = data
        self.prio = None
        self.next = None


def last_number_1(head, m):
    if not head or m < 0:
        return None

    while head.next != head:
        for _ in range(m-1):
            head = head.next
        print "delete:", head.data
        next = head.next
        head.prio.next = head.next
        head.next.prio = head.prio
        head = next

    return head


node0 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node0.next = node1
node1.prio = node0
node1.next = node2
node2.prio = node1
node2.next = node3
node3.prio = node2
node3.next = node4
node4.prio = node3
node4.next = node0
node0.prio = node4

n = last_number_1(node0, 3)


print "-----------"
print "last number:", n.data
print n.next == n
print n.prio == n


'''
解法2：
    首先我们定义一个关于n和m的方程f(n,m)表示每次在n个数字0,1,...,n-1中删除第m个数字最后剩下的数字。
    在这n个数字中，第一个被删除的数字是k=(m-1)%n,则剩下的序列为0,1,...,k-1,k+1,k+2,...,n-1,因为下一次删除从数字k+1开始
计数，则序列相当于k+1,k+2,...,n-1,0,1,2,...,k-1。我们记该序列依次删除第m个数字最后剩下的数字用方程f`(n-1,m)表示。所以有
f(n,m)=f`(n-1,m)。
    但是现在的序列已经并不是从0开始的连续序列了。
    我们将这个序列做一个映射p(x)=(x-k-1)%n,则序列k+1,k+2,...,n-1,0,1,2,...,k-1就被映射为了0,1,2,...,n-2.我们记这个序列
的依次删除第m个数字最后剩下的数字用方程f(n-1,m)表示。
    映射p(x)的逆映射为q(x)=(x+k+1)%n。
    则f(n,m)=f`(n-1,m)=q(f(n-1,m)).
    q(f(n-1,m))=[f(n-1,m) + k + 1] % n.
    因为k=(m-1)%n,则q(f(n-1,m))=[f(n-1,m) + k + 1] % n = [f(n-1, m) + m] % n
    
    经过上面的分析，我们找到了一个递归公式，要得到n个数字的序列中最后剩下的数字，只需要得到n-1的数字的序列最后剩下的数字，以此类推。
当n=1时，也就是序列中开始只有一个数字0时，那么很显然最后剩下的数字就是0.
    我们把这种关系表示为：
             | 0,  当n=1时
    f(n,m) = |
             | [f(n-1, m) + m] % n  当n>1时
'''


def last_number_2(n, m):
    if n < 1 or m < 1:
        return None

    last = 0
    for i in range(2, n+1):
        last = (last + m) % i
    return last


last_number_2(4, 3)
