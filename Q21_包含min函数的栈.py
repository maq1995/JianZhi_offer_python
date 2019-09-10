# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/9 上午11:34
 @desc:
"""
'''
题目:定义栈的数据结构,请在该类型中实现一个能够得到栈的最小元素的min函数.在该栈中,调用min,push,pop的时间复杂度都是O(1)

解析:
    我们的第一反应可能是每次压入一个新元素进栈时,将栈中的所有元素排序,让最小的元素位于栈顶,这样可以在O(1)时间内得到栈的最小元素.
但是这样的话,该数据结构就不是栈了,不满足先进后出的规则了.
    接下来我们想到在栈中添加一个成员变量存放最小的元素,每次压入一个新元素进栈时,如果该元素比当前最小的元素要小,则更新最小元素,
但是如果当前最小的元素出站了,那么接下来的最小元素是多少呢,接下来的最小元素出栈后,下一个最小元素是多少呢?
    所以我们发现仅仅添加一个成员变量是不够的.是不是可以把每次的最小元素都保存在另外一个辅助栈中呢?
    
    例子:
        操作            数据栈            辅助栈                最小值
        -------------------------------------------------------------
        压入3            3                 3                    3
        压入4            3,4               3,3                  3
        压入2            3,4,2             3,3,2                2
        压入1            3,4,2,1           3,3,2,1              1
        弹出             3,4,2             3,3,2                2
        弹出             3,4               3,3                  3
        压入0            3,4,0             3,3,0                0
        
    从上表可以看出,在入栈过程中,如果每次都把最小元素压入辅助栈,那么就能保证辅助栈的栈顶一直都是最小元素.当最小元素从数据栈内被
被弹出之后,同时需要弹出辅助栈的栈顶元素,此时辅助栈的栈顶元素就是下一个最小值.
'''


class minStack:
    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def push(self, data):
        self.data_stack.append(data)
        if len(self.min_stack) == 0 or data < self.min_stack[-1]:
            self.min_stack.append(data)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if self.data_stack and self.min_stack:
            self.min_stack.pop()
            return self.data_stack.pop()
        return None

    def min(self):
        return self.min_stack[-1] if self.min_stack else None


s = minStack()
s.push(3)
s.push(4)
print "the min:", s.min()
s.push(2)
s.push(1)
print "the min:", s.min()
print "pop:", s.pop()
print "pop:", s.pop()
print "the min:", s.min()
s.push(0)
print "the min:", s.min()
print "pop:", s.pop()
print "pop:", s.pop()
print "the min:", s.min()
print "pop:", s.pop()
print "the min:", s.min()
print "pop:", s.pop()
print "the min:", s.min()


