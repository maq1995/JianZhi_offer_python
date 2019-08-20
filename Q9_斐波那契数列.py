# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/20 上午10:49
 @desc:
"""
'''
题目：写一个函数，输入n,求斐波那契数列的第n项。
斐波那契数列的定义如下：
        |  0，  n=0    
f(n) =  |  1,   n=1
        |  f(n-1) + f(n-2),  n>1
        
'''


#  我们最常见的解法如下：
def Fibonacci_dg(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci_dg(n-1) + Fibonacci_dg(n-2)


# print Fibonacci_dg(10)
'''
    上述方法有很严重的效率问题，当n=50时，运行时间就已经很长了。
原因：
    我们以求解f(10)为例来分析递归的求解过程：
              f(10)
           /        \
         f(9)        f(8)
         /    \       /   \
       f(8)   f(7)   f(7)  f(6)
       / \     /   \
    f(7) f(6) f(6)  f(5)

可以看出这个树中有很多结点是重复的，即在计算中也做了很多重复的计算。而且重复的节点数会随着n的增加而急剧增加。
这意味着计算量会随着n的增加而急剧增加。
事实上，用递归方法计算的时间复杂度是以n的指数方式递增的。
            
'''


'''
面试官期待的实用解法：
    改进方法1：上述递归代码之所以慢是因为重复的计算太多，我们只要想办法避免重复计算就行了。比如我们可以把已经得到的数列中间项
              保存起来，如果下次需要计算的时候我们先查找以下，如果前面已经计算过偶就不用在重复计算了。
    改进方法2：更简单的改进方法：从下向上计算，首先根据f(0)和f(1)计算出f(2),在根据f(1)和f(2)计算出f(3)......
              以此类推就可以算出第n项。
'''


# 改进方法2、
def Fibonacci_improved(max):
    if max <= 0:
        return 0
    if max == 1:
        return 1
    n = 0
    a = 0
    b = 1
    while n < max:
        a, b = b, a+b
        n += 1

    return b


# print Fibonacci_improved(10)

'''
关于yield的用法：https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/index.html

清单 1. 简单输出斐波那契數列前 N 个数
        def fab(max): 
           n, a, b = 0, 0, 1 
           while n < max: 
               print b 
               a, b = b, a + b 
               n = n + 1
执行 fab(5)  1  1  2  3  5

结果没有问题，但有经验的开发者会指出，直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。

要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个 List。以下是 fab 函数改写后的第二个版本：

清单 2. 输出斐波那契數列前 N 个数第二版
    def fab(max): 
       n, a, b = 0, 0, 1 
       L = [] 
       while n < max: 
           L.append(b) 
           a, b = b, a + b 
           n = n + 1 
       return L
       
可以使用如下方式打印出 fab 函数返回的 List：
    >>> for n in fab(5): 
    ...     print n 
    ... 
结果：1  1  2  3  5

清单 3. 通过 iterable 对象来迭代
    第二版的fab函数通过返回 List 能满足复用性的要求，但是更有经验的开发者会指出，该函数在运行中占用的内存会随着参数 max 的增大
而增大，如果要控制内存占用，最好不要用 List来保存中间结果，而是通过 iterable 对象来迭代。
例如： Python2中， 代码for i in range(1000):pass 会产生一个1000个元素的List
                 而代码 for i in xrange(1000):pass  不会产生1000个元的List,而是在每次迭代中返回下一个数值，
                 内存空间占用很小。因为xrange不返回List，而是返回一个iterable对象。
                 （Python3中去掉了range（）函数，并将xrange更名为range）
   
清单 4. 第三个版本
    class Fab(object):  
       def __init__(self, max): 
           self.max = max 
           self.n, self.a, self.b = 0, 0, 1 
     
       def __iter__(self): 
           return self 
     
       def next(self): 
           if self.n < self.max: 
               r = self.b 
               self.a, self.b = self.b, self.a + self.b 
               self.n = self.n + 1 
               return r 
           raise StopIteration()              
Fab 类通过 next() 不断返回数列的下一个数，内存占用始终为常数：
    >>> for n in Fab(5): 
    ...     print n 
    ... 
结果：  1  1  2  3  5

然而，使用 class 改写的这个版本，代码远远没有第一版的 fab 函数来得简洁。
如果我们想要保持第一版 fab 函数的简洁性，同时又要获得 iterable 的效果，yield 就派上用场了：

清单 5. 使用 yield 的第四版
    def fab(max): 
        n, a, b = 0, 0, 1 
        while n < max: 
            yield b 
            # print b
            a, b = b, a + b 
            n = n + 1 
第四个版本的 fab 和第一版相比，仅仅把 print b 改为了 yield b，就在保持简洁性的同时获得了 iterable 的效果。
调用第四版的 fab 和第二版的 fab 完全一致：
    >>> for n in fab(5): 
    ...     print n 
    ... 
结果：1  1  2  3  5

  ！！！！！简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器
会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会
执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，
而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。

也可以手动调用 fab(5) 的 next() 方法（因为 fab(5) 是一个 generator 对象，该对象具有 next() 方法），这样我们就可以更清楚
地看到 fab 的执行流程：


清单 6. 执行流程
    >>> f = fab(5) 
    >>> f.next() 
    1 
    >>> f.next() 
    1 
    >>> f.next() 
    2 
    >>> f.next() 
    3 
    >>> f.next() 
    5 
    >>> f.next() 
    Traceback (most recent call last): 
     File "<stdin>", line 1, in <module> 
    StopIteration

当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。
在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。


我们可以得出以下结论：
    一个带有 yield 的函数就是一个generator，它和普通函数不同，生成一个generator看起来像函数调用，但不会执行任何函数代码，
直到对其调用next()（在for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句
就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了
数次，每次中断都会通过 yield 返回当前的迭代值。
    yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个next()的
值，不仅代码简洁，而且执行流程异常清晰。

如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：


清单 7. 使用 isgeneratorfunction 判断
    >>> from inspect import isgeneratorfunction 
    >>> isgeneratorfunction(fab) 
    True

要注意区分 fab 和 fab(5)，fab是一个generator function，而fab(5)是调用fab返回的一个 generator，
好比类的定义和类的实例的区别：
清单 8. 类的定义和类的实例
    >>> import types 
    >>> isinstance(fab, types.GeneratorType) 
    False 
    >>> isinstance(fab(5), types.GeneratorType) 
    True
fab 是无法迭代的，而 fab(5) 是可迭代的：
    >>> from collections import Iterable 
    >>> isinstance(fab, Iterable) 
    False 
    >>> isinstance(fab(5), Iterable) 
    True
每次调用 fab 函数都会生成一个新的 generator 实例，各实例互不影响：
    >>> f1 = fab(3) 
    >>> f2 = fab(5) 
    >>> print 'f1:', f1.next() 
    f1: 1 
    >>> print 'f2:', f2.next() 
    f2: 1 
    >>> print 'f1:', f1.next() 
    f1: 1 
    >>> print 'f2:', f2.next() 
    f2: 1 
    >>> print 'f1:', f1.next() 
    f1: 2 
    >>> print 'f2:', f2.next() 
    f2: 2 
    >>> print 'f2:', f2.next() 
    f2: 3 
    >>> print 'f2:', f2.next() 
    f2: 5

return 的作用
    在一个 generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，则直接抛出 
StopIteration 终止迭代。

另一个例子
    另一个yield的例子来源于文件读取。如果直接对文件对象调用read()方法，会导致不可预测的内存占用。好的方法是利用固定
长度的缓冲区来不断读取文件内容。通过yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取：
清单 9. 另一个 yield 的例子
    def read_file(fpath): 
       BLOCK_SIZE = 1024 
       with open(fpath, 'rb') as f: 
           while True: 
               block = f.read(BLOCK_SIZE) 
               if block: 
                   yield block 
               else: 
                   return
'''


# 根据上述关于yeild的介绍，我们可以将斐波那契数列函数改写为：
def Fibonacci_improved2(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1


# 或者
def fib(num):
    a, b = 0, 1
    for i in xrange(num):
        yield b
        a, b = b, a+b
