# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/14 下午4:02
 @desc:
"""
'''
题目：用两个栈实现一个队列。
请实现它的两个函数appendTail和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。
'''

'''
    使用一个具体的例子来分析往该队列中插入和删除元素的过程。
    首先插入一个元素a,不妨先把它插入到stack1中，此时stack1中的元素为{a}，stack2为空，再插入两个元素b和c,则此时stack1
的元素为{a,b,c},而stack2仍然是空的。此时尝试着从队列中删除一个元素，按照队列先入先出的规则，由于a,比b,c先到，所以最先被
删除的元素应该是a,但是现在a并不在栈顶，因此不能直接删除。注意！，此时stack2还是空的，我们将stack1中的元素逐个pop出来，
并push到stack2中，此时stack1为空，stack2中的元素正好和之前stack1中顺序相反，为{c,b,a},这个时候就可以弹出stack2栈顶的
元素a了，然后我们再弹出b,此时stack1为空，stack2为{c}.接着再插入一个元素d,我们还是把它压入到stack1中，此时stack1中的元素
为{d},stack2中的元素为{c}, 如果要出队的话，还是从stack2中弹出数据，此时stack1：{d},stack2:{},如果还要出队的话，因为
stack2为空，所以先将stack1中的元素逐个弹出并压入到stack2中再弹出。  

    插入： 往stack1中插入即可 
    删除的步骤：当stack2不为空时，在stack2中的栈顶元素就是最先入队列的元素，可以弹出，
              当stack2为空，就把stack1中的元素逐个弹出并压入stack2中，此时stack2不为空，且stack2栈顶为最先入队的元素，
              可以弹出。
'''


class m_queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, data):
        self.stack1.append(data)

    def deleteHead(self):
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return False
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

            return self.stack2.pop()
        else:
            return self.stack2.pop()


queue = m_queue()
queue.appendTail(3)
queue.appendTail(5)
queue.appendTail(-1)
print queue.deleteHead()
print queue.deleteHead()
print queue.deleteHead()
print queue.deleteHead()
