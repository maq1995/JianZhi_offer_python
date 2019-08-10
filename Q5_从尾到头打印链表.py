# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/9 上午10:44
 @desc:题目： 输入一个链表的头结点，从尾到头反过来打印出每个结点的值。
"""
'''
链表的结点定义如下：
struct ListNode{
    int m_nKey;
    ListNode* m_pNext;
};
'''


# Python中没有内置ListNode的实现，首先需要实现一个链表类
class Node(object):
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        return str(self.data)


class ChainTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:  # 头指针是空的
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        if self.isEmpty():
            print "this chain table is empty"
            return
        if index < 0 or index>= self.length:
            print "error: out of index"
            return

        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            prev._next = node._next
            self.length -= 1

    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print 'this chain table is empty'
            return

        if index < 0 or index >= self.length:
            print "error: out of index"
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j ==index:
            item._next = node
            prev._next = item
            self.length += 1

    def update(self, index, data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print "error:out of index"
            return

        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        if j == index:
            node.data = data

    def getItem(self, index):
        if self.isEmpty() or j < 0 or j >= self.length:
            print "error: out of index"
            return

        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        return node.data

    def getIndex(self, data):
        j = 0
        if self.isEmpty():
            print "this chain table is empty"
            return
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1

        if j == self.length:
            print "{} not found".format(data)
            return

    def clear(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            return "empty chain table"
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist

    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print "error: out of index"
            return
        return self.getItem(ind)

    def __setitem__(self, ind, val):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print "error: out of index"
            return
        self.update(ind, val)

    def __len__(self):
        return self.length


'''
从尾到头打印链表：
    从头到尾打印链表会很简单，通常打印是一个只读操作，我们不希望打印时修改链表（即将链表指针翻转）。
    遍历链表的顺序是从头到尾，打印的顺序是从尾到头，也就是所第一个遍历到的结点最后一个输出，而最后一个遍历到的结点第一个输出，
这就是典型的“先进后出”，我们可以使用栈来完成这种顺序。每经过一个结点的时候，把该结点放到一个栈中，当遍历完整个链表后，再从栈顶
开始逐个输出结点的值。
'''


# 创建一个链表
ct = ChainTable()
node1 = Node(3)
node2 = Node(25)
node3 = Node(0)
node4 = Node(12)
node5 = Node(77)
node6 = Node(52)
ct.append(node1)
ct.append(node2)
ct.append(node3)
ct.append(node4)
ct.append(node5)
ct.append(node6)


def reverse_print_chain_table(chain_table):
    if chain_table.isEmpty():
        print "this chain table is NULL!"
        return

    s = []
    while not chain_table.isEmpty():
        # print "chain_table:", chain_table
        node = chain_table.head
        # print "node:", node
        s.append(node.data)
        # print "s:", s
        chain_table.head = node._next
        chain_table.length -= 1
        # print "chain_table:", chain_table
        # print "chain_table.isempty:", chain_table.isEmpty()
        # print "\n"

    while len(s) != 0:
        # print "s:", s
        print s.pop()


# 添加测试用例：
# 1.输入的链表含有多个结点
# 2.输入的链表只有一个结点
# 3.输入的链表头指针为空
# reverse_print_chain_table(ct)  # 1
# print "\n"
node7 = Node(2)
ct2 = ChainTable()
ct2.append(node7)
# reverse_print_chain_table(ct2)  # 2
# print '\n'
ct3 = ChainTable()
# reverse_print_chain_table(ct3)  # 3
#

'''
思路2：   递归   
    既然想到了使用栈来实现这个函数，而递归在本质上就是一个栈结构，于是很自然的想到用递归来实现。要实现反过来输出链表，我们每访问到
一个结点的时候，先递归输出它后面的结点，在输出该结点自身，这样链表的输出结果就反过来了。
'''


def digui_reverse_print_chain_table(chain_table):
    if chain_table.isEmpty():
        print "this chain table is NULL!"
        return
    node = chain_table.head
    if node is not None:
        if node._next is not None:
            chain_table.head = node._next
            digui_reverse_print_chain_table(chain_table)
        print node.data


digui_reverse_print_chain_table(ct)
print "\n"
digui_reverse_print_chain_table(ct2)
print "\n"
digui_reverse_print_chain_table(ct3)













