# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/16 下午2:31
 @desc:
"""
'''
题目：输入两个单向链表，找出它们的第一个公共结点。

解析：
    这两个链表是单向链表，如果两个单向链表有共同的结点，那么这两个链表从某一结点开始，它们的next指针都指向同一个结点，由于单向
链表的结点只能有一个next，因此从第一个公共结点开始，之后它们的所有结点都是重合的，不可能再出现分叉。所以两个有公共结点而部分重合
的链表，拓扑形状看起来像一个Y。
    我们有两种思路：
    思路1：分别把两个链表的结点放入到两个栈中，这样两个链表的尾结点就位于两个栈的栈顶，接下来比较两个栈顶的结点是否相同，如果相
          同则把栈顶元素弹出接着比较下一个栈顶，直到找到最后一个相同的结点。
          
    思路2：我们可以先遍历两个链表得到它们的长度，得到长的链表比短的链表多几个结点，在第二次遍历的时候，在长链表上先走若干步，然后
          再开始同步遍历，找第一个相同的结点
'''


class ChainTableNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_first_same_node_1(head1, head2):
    if not head1 or not head2:
        return None
    stack1 = []
    stack2 = []

    while head1:
        stack1.append(head1)
        head1 = head1.next

    while head2:
        stack2.append(head2)
        head2 = head2.next

    same_node = None
    i = len(stack1) - 1
    j = len(stack2) - 1
    while i >= 0 and j >= 0:
        if stack1[i] == stack2[j]:
            same_node = stack1[i]
            i -= 1
            j -= 1

        else:
            break

    return same_node


def find_first_same_node_2(head1, head2):
    if not head1 or not head2:
        return None
    move1, move2 = head1, head2
    lenght1 = 0
    while move1:
        lenght1 += 1
        move1 = move1.next
    lenght2 = 0
    while move2:
        lenght2 += 1
        move2 = move2.next

    while lenght1 > lenght2:
        lenght1 -= 1
        head1 = head1.next
    while lenght2 > lenght1:
        lenght2 -= 1
        head2 = head2.next

    while head1:
        if head1 == head2:
            return head1
        else:
            head1 = head1.next
            head2 = head2.next
    return None


node1 = ChainTableNode(1)
node2 = ChainTableNode(2)
node3 = ChainTableNode(3)
node4 = ChainTableNode(4)
node5 = ChainTableNode(5)
node6 = ChainTableNode(6)
node7 = ChainTableNode(7)
node1.next = node2
node2.next = node3
node3.next = node6
node6.next = node7

node4.next = node5
node5.next = node6


# node = find_first_same_node_1(node1, node4)
node = find_first_same_node_2(node1, node4)
if node:
    print node.data
else:
    print "No same node"



