# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/10 上午11:04
 @desc:
"""
'''
题目：输入一个字符串，打印出该字符串中字符的所有排列。  即求全排列
     例如输入字符串abc,则打印出有字符a、b、c所能排列出来的所有字符串：abc,acb,bac,bca,cab,cba
     
解析：
    # 把字符串分为两部分，一部分是字符串的第一个字符，另一部分是第一个字符以后的所有字符。
    # 首先求所有可能出现在第一个位置的字符，即：将第一个字符和后面所有的字符交换。然后把后面的字符串作为新的字符串，重复上述操作。
#    下面的代码不是用这个思想
'''


# def my_permutation(s):
#     str_set = []
#     ret = []  # 最后的结果
#
#     def permutation(string):
#         for i in string:
#             str_tem = string.replace(i, '')
#             str_set.append(i)
#             if len(str_tem) > 0:
#                 permutation(str_tem)
#             else:
#                 ret.append(''.join(str_set))
#             str_set.pop()
#
#     permutation(s)
#     return ret


def Permutation(ss):
    if not ss:
        return []
    if len(ss) == 1:
        return list(ss)
    pStr = []
    charlist = list(ss)
    charlist.sort()

    for i in range(len(charlist)):
        if i > 0 and charlist[i] == charlist[i - 1]:
            continue
        ll = ''.join(charlist[:i])
        rr = ''.join(charlist[i + 1:])

        temp = Permutation(''.join(charlist[:i]) + ''.join(charlist[i + 1:]))
        for j in temp:
            tt = charlist[i] + j
            pStr.append(tt)
    return pStr


# 简化版本
def perm(s):
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in perm(s[0:i] + s[i + 1:]):
            sl.append(s[i] + j)
    return sl


# str = 'abc'
# print perm(str)


#  网址：  https://blog.csdn.net/sty945/article/details/79839567


'''
扩展： 如果不是求字符的全排列，而是求字符的所有组合。还是输入三个字符abc,则它们的组合有a,b,c,ab,ac,bc,abc.当交换字符串中的
     两个字符时，虽然能得到两个不同的排列，但确实同一个组合，如ab和ba是不同的排列，但只能算一个组合。
'''


def get_combinations(string):
    combs = []
    for i in range(1, 2**len(string)):
        # "{0:b}".format(i) 产生i的二进制
        pat = "{0:b}".format(i).zfill(len(string))  # zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
        combs.append(''.join(c for c, b in zip(string, pat) if int(b)))
    return combs


str = 'abc'
print get_combinations(str)
