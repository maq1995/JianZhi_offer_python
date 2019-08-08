# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/8 下午4:14
 @desc: 题目： 请实现一个函数，把字符串中的的每个空格替换成“%20”.例如，输入“We are happy”，则输出“We%20are%20happy”
    在网络编程中，如果ＵＲＬ参数中含有特殊字符，如空格、＃等，可能导致服务器端无法获得正确的参数值。我们需要将这些特殊符号转换
成服务器可以识别的字符。转换的规则是在％后面跟上ASCII码的两位十六进制的表示。比如空格的ASCII码值是32，即十六进制的0x20，因此
空格倍替换为%20，再比如#的ASCII码值是35，即十六金子的0x23，它在URL中倍替换为%23.

"""

'''
分析：
    1.因为字符串是不可变对象，所以在实现之前，应该先弄清楚，是在原来的字符串上做替换（可能覆盖修改在该字符串后面的内存），还是创建
新的字符串并在新的字符串上做替换（我们可以自己分配足够多的内存）。这里假设是在原来的字符串上做替换，并保证输入的字符串后面有足够的空余
内存。
    2.思路：
        遍历字符串，遇到空格时，将其替换为%20,因为之前空格占一个字符位，现在%20占3个字符，需要将后面的字符向后移。自然想到从后向前
进行字符串遍历。
    具体：先遍历一遍字符串，统计出空格的个数，则最终字符串的长度=现有字符串长度+2×空格个数。然后准备两个指针，P1和P2,P1指向原始
字符串的末尾，P2指向替换之后的更长的字符串的末尾，然后将P1指向的字符一个一个复制到P2处，每复制一个字符，两个指针都向前移动一位，
直到遇到空格停止，将%20填充之后，将P1和P2移动到相应位置，再次开始复制过程。
'''


# ！！！未实现功能！！！
def fill_blank(s):
    length = len(s) - 1
    count = 0
    for i in range(length):
        if s[i] == ' ':
            count += 1
    new_length = length + count*2
    while length >= 0:
        if s[length] != ' ':
            s[new_length] = s[length]  # Wrong！！！ python 中字符串不支持item assignment
            length -= 1
            new_length -= 1
        else:
            s[new_length - 2: new_length] = '%20'
            new_length = new_length - 2
            length -= 1
    return s


'''
python 的字符串不支持item assignment, 可以进行切片
但是切片会创建新的字符串。 new = s[:i] + s[(i+1):]
但是在使用后向遍历可以不创建新的字符串
具体实现方式需要改变，
思路：
    后向遍历字符串，记录指针移动的步数，当遇到空格是，先暂停，然后将指针之前的字符串切片（不包含空格）+“%20”+指针之后的字符串切片
'''


def fill_blank_2(s):
    if s is None:
        return False
    else:
        i = len(s)-1
        while i >= 0:
            if s[i] != ' ':
                i -= 1
            else:
                s = s[:i] + '%20' + s[i+1:]
                i -= 1
        return s


'''
！！！ python中str有replace方法，可以直接使用。
'''


# 使用Python自带的的replace方法
def fill_blank_1(s):
    return s.replace(' ', '%20')


'''
添加测试用例：
包括：
    1.输入的字符串包括空格：空格位于字符串最前面、最后面、中间（字符串中间有多个连续空格）
    2.输入的字符串没有空格
    3.特殊输入测试：字符串是NULL， 字符串只有一个空格字符、字符串只有个多个连续空格
'''

# string = ' We   are happy '
# string = 'ihavenoblank'
# string = ' '  # 一个空格
# string = '   '  # 3个空格
string = ''
print fill_blank_2(string)

