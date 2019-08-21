# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/20 下午3:39
 @desc:
"""
"""
题目：在Excel2003中，用A表示第1列，B表示第2列......Z表示第26列，AA表示第27列，AB表示第28列......以此类推。
    请写出一个函数，输入用字母表示的列号编码，输出它是第几列。

解析：
    这是一道关于进制的题目，其本质是把十进制数字用A-Z表示成二十六进制。
    
进制转换：
    m进制转换为十进制：
        (第0位 × m^0) + (第1位 × m^1) + (第2位 × m^2) + ....
        例子： 二进制转换为十进制
            1110  
            十进制： 0*2^0 + 1×2^1 + 1×2^2 + 1×2^3 = 14
    十进制转换为m进制：
        除m取余法
        例子： 十进制转换为2进制
            14
        14 / 2 = 7 。。。0
        7 / 2 = 3。。。1
        3 / 2 = 1。。。 1
        1 / 2 = 0。。。1
        则14对应的二进制为1110
"""
"""
A的ASCII码值为65
Python中输出字符的ASCII码值： ord('A')  = 65
Python中输出ASCII码值对应的字符： chr(65)  ='A'
"""


def lieshu(str):
    l = list(str)
    l.reverse()
    print l
    num = 0
    for i in range(len(l)):
        num += (ord(l[i]) - 64) * 26**i
    return num


print lieshu('AB')


