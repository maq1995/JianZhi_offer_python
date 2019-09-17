# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/17 上午9:50
 @desc:
"""
'''
题目1：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一起处理。
     例如输入字符串“I am a student.”，则输出“student. a am I”

解析：
    第一步：翻转句子中所有的字符，比如翻转“I am a student.”中的所有字符得到“.tneduts a ma I”。此时不但翻转了句子中单词的顺序，
           连单词内的字符顺序也被翻转了
    第二步：翻转每个单词中字符的顺序，得到“student. a am I”
    
    python中的字符串是不可变对象
'''


# 利用Pythont特性
def Reverse(s):
    temp = s.split()
    if len(temp) == 0:
        return s
    return ' '.join(s.split()[::-1])


# print Reverse('I am a student.')


# 两次翻转法
def Reverse_twice(s):
    if not s:
        return None

    l1 = list(s)
    l1 = l1[::-1]
    # print l1

    start = 0
    end = 0
    ret = []
    while end < len(l1):
        if end == len(l1) - 1:
            ret.append(''.join(l1[start:][::-1]))
        if l1[end] == ' ':
            ret.append(''.join(l1[start:end][::-1]))
            start = end + 1
        if l1[start] == ' ':
            start += 1
            end += 1
            ret.append([' '])
        else:
            end += 1

    print ret


# Reverse_twice('I am a student.')


'''
题目2：字符串的左旋操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转的功能。
      例如输入字符串“abcdefg”和数字2，则该函数返回左旋转2位得到的结果“cdefgab”
      
解析：
    在上面的问题中的第一步里，将整个字符串翻转。
    本题中我们可以将字符串分为两个部分，先分别将两个部分的字符串翻转，然后再作为一个整体翻转。
    例如输入“abcdefg”, 数字为2，则将字符串分为“ab”，“cdefg”两个部分，分别翻转两部分变为：“ba”，“gfedc”,然后将这两部分
作为整体“bagfedc”再翻转得到“cdefgab”
'''


# 利用Python 特性
def left_rotate(string, n):
    if not string:
        return None
    n %= len(string)
    return string[n:] + string[:n]


# print left_rotate('abcdefg', 2)


# 翻转法
def left_rotate_2(string, n):
    if not string:
        return None
    if len(string) <= n:
        return string

    l1 = list(string)
    left = l1[:n][::-1]
    right = l1[n:][::-1]
    ret = (left + right)[::-1]
    return "".join(ret)


print left_rotate_2('abcdefg', 2)
