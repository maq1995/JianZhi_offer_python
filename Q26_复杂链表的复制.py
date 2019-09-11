# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/10 上午8:58
 @desc:
"""
'''
题目：请实现函数ComplexListNode* Clone(ComplexListNode* pHead),复制一个复杂链表。
     在复杂链表中，每个结点除了有一个next指针指向下一个结点外，还有一个Sibling指针指向链表中的任意结点或者NULL

解析：
    1.暴力方法是先复制原始链表上的每个结点，并用next指针连接起来，然后就是设置每个结点的sibling指针。假设原始链表中某个结点N
      的Sibling结点为S，那么S有可能在N的前面或后面，所以定位S需要从原始链表的头结点沿着next指针开始寻找，假设经过m步找到结点S
      ，那么在复制链表中，N`的Sibling指针指向的S`也是从头结点开始经过m步找到的结点。
      但是暴力方法的时间复杂度为O（n^2）.因为对于一个含有n个结点的链表，对于每一个结点都需要寸照其Sibling，时间复杂度为O（n）。
    2.在不适用辅助空间的情况下实现O（n）的时间效率
      step1：根据原始链表的每个结点N创建对应的N`，将N`连接在N的后面。
      step2：设置复制结点的Sibling。假设原始链表上的N的Sibling指向结点S，那么其对应的复制结点N`的Sibling指向的结点应该是S的
             复制结点S`.
      step3：把长链表拆分为两个短链表。把奇数位置上的结点用next指针连起来就是原始链表，把偶数位置上的结点用next指针连起来就是复制
             出来的链表。
'''


# 结点定义
class ComplexListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.sibling = None


def complexListColon(head):
    if not head:
        return None
    # 第一步： N对应的N`，将N`连接在N的后面
    node = head
    while node:
        colonNode = ComplexListNode(node.data)
        colonNode.next = node.next
        node.next = colonNode
        node = colonNode.next

    # 第二步： 设置N`的Sibling
    node1 = head
    while node1:
        colonNode1 = node1.next
        if node1.sibling is not None:
            colonNode1.sibling = node1.sibling.next
        node1 = colonNode1.next

    # 第三步： 分解长链表
    node2 = head
    colonHead = None
    colonNode2 = None
    if node2:
        colonHead = colonNode2 = node2.next
        node2.next = colonHead.next
        node2 = node2.next
    while node2:
        colonNode2.next = node2.next
        colonNode2 = colonNode2.next
        node2.next = colonNode2.next
        node2 = node2.next

    return colonHead


# n1 = ComplexListNode("A")
# n2 = ComplexListNode("B")
# n3 = ComplexListNode("C")
# n4 = ComplexListNode("D")
# n5 = ComplexListNode("E")
# n1.next = n2
# n1.sibling = n3
# n2.next = n3
# n2.sibling = n5
# n3.next = n4
# n4.next = n5
# n4.sibling = n2

# n1 = ComplexListNode("A")

# n1 = ComplexListNode("A")
# n1.sibling = n1

n1 = ComplexListNode("A")
n2 = ComplexListNode("B")
n1.next = n2
n1.sibling = n2
n2.sibling = n1

result = complexListColon(n1)

while result:
    if result.next and result.sibling:
        print result.data, result.next.data, result.sibling.data
    elif result.next:
        print result.data, result.next.data
    elif result.sibling:
        print result.data, result.sibling.data
    else:
        print result.data
    result = result.next
