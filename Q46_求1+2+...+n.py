# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/18 下午2:15
 @desc:
"""
'''
题目：求1+2+...+n。要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句。

分析：
    通常求1+2+...+n除了用公式n(n+1)/2之外，还有循环和递归，但是循环会涉及到for、while的使用，递归涉及到if语句来判断是否继续
递归下去。
'''


'''
解法1：
    利用Python特性
'''


def SumOf1ToN(n):
    return sum(range(1, n+1))


'''
解法2：
    使用reduce函数
'''


def SumOf1ToN_2(n):
    return reduce(lambda x, y: x+y, range(n+1))


# print SumOf1ToN_2(5)

'''
解法3：
    利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况。如果对n连续进行两次反操作（即!!n），那么非零的n转
换为True，0转换为False。
'''


# 递归函数
def sum_digui(n):
    func = {False:sum0, True:sum_digui}
    return n+func[not not n](n-1)


def sum0(n):
    return 0


# print sum_digui(6)



