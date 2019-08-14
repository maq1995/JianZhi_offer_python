# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/14 下午4:39
 @desc:
"""
'''
    用一个例子来说明怎么使用两个队列实现一个栈。
    queue1和queue2，入栈元素a,b,c,(假设使用queue1),那么此时queue1：{a,b,c}，queue2：{}，
    如果此时想要出栈，那么弹出的应该是c,但是queue1,2都只能先进先出，则queue1出队a,再将a入队queue2，queue1出队b,在将b入队queue2.
此时queue1：{c},queue2:{a,b},此时queue1再出队，则结果为c。
    此时queue1：{},queue2:{a,b}，如果此时要入栈d,则向queue2中插入，那么queue1：{}，queue2：{a,b,d},
    此时想要出栈，结果应该是d,方法一样，queue2出队a,将a入队queue1，queue2出队b,将b入队queue1，然后queue2再出队，则结果为d.
    此时queue1:{a,b}, queue2：{}，此时再出栈，queue1出队a,将a入队queue2,queue1再出队即为b,

总结：
    push： 向非空队列入队即可，如果两个队列均为空，任意选择一个。
    pop：将非空队列中的元素一个一个出队，并将其入队到另一个队列中，直到非空队列只剩一个元素，然后将该元素出队即可。
'''


class m_stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, data):
        if len(self.queue2) == 0:
            self.queue1.append(data)
        if len(self.queue1) == 0:
            self.queue2.append(data)

    def pop(self):
        if not self.queue1 and not self.queue2:
            return False
        if len(self.queue1) != 0:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        if len(self.queue2) != 0:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()


stack = m_stack()
stack.push(3)
stack.push(22)
stack.push(-9)
print stack.pop()
print stack.pop()
print stack.pop()
print stack.pop()
