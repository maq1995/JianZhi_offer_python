# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/16 上午8:48
 @desc:
"""
'''
题目：在字符串中找出第一个只出现一次的字符，如输入“abaccdeff”,则输出'b'.

解析：
    由于题目与字符出现的次数相关，我们可以统计每个字符在该字符串中出现的次数。使用哈希表。
    哈希表的Key是字符，value是该字符出现的次数。我们需要从头扫描两次字符串：第一次扫描字符串时，每扫描到一个字符就在哈希表中
的对应项将次数加1，第二次扫描时，每扫描到一个字符就从哈希表中得到该字符出现的次数，这样，第一个只出现一侧的字符就找到了。
    另外：哈希表在Python中对应的是字典！！！
'''


def first_once_appearing(string):
    if len(string) <= 0:
        return None
    dict = {}
    # 第一遍遍历
    for s in string:
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1

    # 第二遍遍历
    for index, value in enumerate(string):
        if dict[value] == 1:
            return value
    return None


# s = 'abaccdeff'
# s1 = 'ababcdcdefef'
# s2 = ''
# print first_once_appearing(s2)


'''
相关题目1：定义一个函数，输入两个字符串，从第一个字符串中删除在第二个字符串中出现过的所有字符。例如从第一个字符串“We are 
        students”中删除第二个字符串“aeiou”中出现过的字符得到的结果为：“W r stdnts”.
        
解析：
    为了解决这个问题，我么可以创建一个用数组实现的简单哈希表来存储第二个字符串，这样我们从头到尾扫描第一个字符串中的每一个字符
时，用O（1）时间就能判断出该字符是不是在第二个字符中。如果第一个字符串的长度为n,那么总的时间复杂度为O（n）.
'''


def delete_char_in_second_string(string1, string2):
    if len(string1) <= 0:
        return None
    if len(string2) <= 0:
        return string1

    # 第二个字符串用哈希表存储
    dict = {}
    for s in string2:
        dict[s] = 1

    l1 = []
    for j in string1:
        if j not in dict:
            l1.append(j)

    string1 = "".join(l1)
    return string1


# s1 = 'We are students'
# s2 = 'aeiou'
# print delete_char_in_second_string(s1, s2)


'''
相关题目2：定义一个函数，删除字符串中所有重复出现的字符。例如输入‘google’,删除重复的字符之后的结果是‘gole’。


解析：
    这个题目和上面的问题比较类似，我们可以创建一个用布尔型数组实现的简单的哈希表，表示该字符在字符串中是否已经出现。
'''


def delete_repitation_char(string):
    if len(string) <= 1:
        return string
    dict = {}
    l1 = []
    for s in string:
        if s not in dict:
            dict[s] = 1
            l1.append(s)

    string = ''.join(l1)
    return string


# s = 'google'
# s1 = 'ma qian'
# print delete_repitation_char(s1)


'''
相关题目3：在英语中，如果两个单词中出现的字母相同，并且每个字母的出现次数也相同，那么这两个单词互为变位词。例如listen和silnet,
        evil和live等互为变位词。请完成一个函数，判断输入的两个字符是不是互为变位词。
        
解析：
    我们可以创建一个用数组实现的简单哈希表，用来统计字符串中每个子出现的次数。当扫描到第一个字符串中的每个字符时，为哈希表对应的
值加1，扫描第二个字符串时，为哈希表对应的值减1.如果扫描完第二个字符串后，哈希表中所有的值都是0，那么这两个字符串就互为变位词。
'''


def is_Anagram(string1, string2):
    if len(string1) <= 0 or len(string2) <= 0:
        return False
    if len(string1) != len(string2):
        return False

    dict = {}
    for s1 in string1:
        if s1 in dict:
            dict[s1] += 1
        else:
            dict[s1] = 1

    for s2 in string2:
        if s2 in dict:
            dict[s2] -= 1

    flag = True
    for key in dict:
        if dict[key] != 0:
            flag = False

    return flag


# s1 = 'listen'
# s2 = 'silent'

s1 = 'hello'
s2 = 'olle'
print is_Anagram(s1, s2)