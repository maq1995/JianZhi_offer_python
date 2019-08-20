# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/20 下午3:21
 @desc:
"""
'''
题目：我们可以用2行1列的小矩形横着或者竖着去覆盖更大的矩形。
    请问用8个这样的2*1的小矩形无重叠地覆盖一个2行8列的大矩形，共有多少种方法？

解析：
    我们先把2*8的覆盖方法记为f(8),用第一个2*1的小矩形覆盖大矩形的最左边时，我们有两种选择：横着放，或者竖着放。
    当竖着放时，右边还剩2*7的区域，这种情形下的覆盖方法记为f(7), 当横着放时，1*2的小矩形放在左上角时，左下角也
必须横着放一个1*2的小矩形，此时右边还剩2*6的区域，这种情形下的覆盖方法记为f(6),即 f(8) = f(7) + f(6)
    即：斐波那契数列 
'''


def matrix_cover():
    n, a, b = 0, 0, 1
    while n < 8:
        a, b = b, a+b
        n += 1
    return b


print matrix_cover()

