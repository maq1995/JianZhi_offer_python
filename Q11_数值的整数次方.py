# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/21 上午9:13
 @desc:
"""
'''
题目：实现函数double Power(double base, int exponent),求base的exponent次方，不得使用库函数，同时不需要考虑大数问题
'''

'''
解析：
    第一眼感觉这个题很简单,做exponent次base的乘法即可
    
    但是有问题
'''
def Power(base, exponent):
    result = 1
    for _ in xrange(exponent):
        result = result*base

    return result

# print  Power(0, -1)
"""
问题：
    1.没有考虑指数为负数的情况：指数为负数时，先对指数求绝对值，求完幂之后，求倒数即可
        1.1.求倒数，应该意识到如果数为0，求倒数该怎么办
    2.当底数为0，指数为0的情况，结果应该等于多少  (等于0或1都可以) 
    3.当底数为0时，0的多少次方都是0。
    4.因为本题要求的base是double类型的，所以如果判断base是否等于0，不能用==做判断，因为在计算机内表示小数时都有误差。
    判断两个小数是否相等，应该用equal函数,Python中没有equal函数，
    在Python2中，判断两个浮点数是否相等，abs(a-b) < 1.0e-9 就认为a等于b了。
    在Python3中，使用math.isclose(a,b)
"""


# 解决问题
def Power_improved(base, exponent):
    if abs(base - 0.0) < 1e-9 and exponent < 0:
        print "Invalid input"
        return
    if abs(base - 0.0) < 1e-9 and exponent >= 0:
        return 0

    result = 1
    abs_exponet = abs(exponent)
    for _ in xrange(abs_exponet):
        result = result * base

    if exponent < 0:
        result = 1.0 / result
        return result
    elif exponent > 0:
        return result


# print Power_improved(0, -2)


'''
改进：
    如果输入的指数exponent是32，我们就需要做31次乘法。但是我们可以换一个思路：我们的目标是求出一个数的32次方，如果我们已经知道
它的16次方，那么只要在16次方的基础上再平方一次即可。同样，16次方是8次方的平方，8次方是4次方的平方...以此类推。我们求32次方就只
需要5次乘法即可。
    也就是我们可以用下面的公式求a的n次方。
          |  a^(n/2) * a^(n/2)，   当n是偶数时
    a^n = |
          |  a^[(n-1)/2] * a^[(n-1)/2] * a,    当n是奇数时
          
    另外，使用右移操作代替除以2的操作，用位与运算代替求余运算（%）来判断一个数是奇数还是偶数。因为位运算的效率比乘除法及求
余的效率要高。
'''


def power_final_version(base, exponent):
    if equal_zero(base) and exponent < 0:
        print "Invalid input"
        return
    if equal_zero(base) and exponent >= 0:
        return 0

    abs_exponent = abs(exponent)
    result = power_value(base, abs_exponent)
    if exponent < 0:
        return 1.0 / result
    else:
        return result


def equal_zero(base):
    if abs(base - 0.0) < 1e-9:
        return True
    return False


def power_value(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    result = power_value(base, exponent >> 1)
    result *= result

    if exponent & 1 == 1:  # exponent是奇数
        result *= base
    return result


print power_final_version(2, 10)
