# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/21 上午8:15
 @desc:
"""
'''
题目1：用一条语句判断一个整数是不是2的整数次方。
解析：
    一个整数如果是2的整数次方，那么它的二进制表示中有且只有一位是1，而其他所有位都是0.
    根据Q10_，把这个整数减去1之后再和它自己做与运算，这个整数中唯一的1会变成0
'''


def is_2_mi(n):
    return n & (n-1) == 0


# print is_2_mi(8)


'''
题目2：输入两个整数m和n,计算需要改变m的二进制表示中的多少位才能得到n.比如10的二进制表示为1010,13的二进制表示为1101，需要改变1010
      中的3位才能得到1101.
解析：
    我们可以分两步来解决这个问题，第一步：求这两个数的异或，第二步，统计异或结果中1的位数
'''


def m_to_n(m, n):
    num = m ^ n
    count = 0
    if num == 0:
        return count
    while num != 0:
        count += 1
        num = num & (num - 1)
    return count


print m_to_n(10, 14)
