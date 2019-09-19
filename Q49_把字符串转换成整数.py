# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/18 下午4:01
 @desc:
"""
'''
题目：实现一个函数，把字符串转换成整数这个功能。

解析：
    将字符串转换成整数，说明字符串包含的是'0'~'9',注意还可以包含’+‘，’-‘，如果包含除此以外的字符就是非法的。
    另外，Python中没有整数溢出的概念，所以不用考虑溢出。
'''


def StrToInt(string):
    if not string:
        raise Exception('String cannot be None', string)

    ret = 0
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    label = 1
    for i in range(len(string)):
        if i == 0:
            if string[i] == '+':
                continue
            if string[i] == '-':
                label = -1
                continue
        if string[i] in nums:
            b = string[i]
            a = ord(string[i])
            ret = ret*10 + (ord(string[i]) - ord('0'))
        else:
            raise Exception("String are illegal", string)

    return label*ret


print StrToInt('shjdiuinf')




