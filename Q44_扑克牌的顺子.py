# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/18 上午9:19
 @desc:
"""
'''
题目：从扑克牌中随机抽取5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2~10为数字本身，A为1，J为11，Q为12，K为13，
     而大小王可以看出任意数字。
     
解析：
    怎么判断这5个数字是不是连续的最直观的方式是把数组排序。由于在本题中，0可以被看作任意数字，我们可以用0去补满数组中的空缺，
如果排序之后的数字不是连续的，即相邻的两个数字相隔若干个数字，但只要我们有足够的0可以补满这两个数字的空缺，这个数组实际上还是
连续的。例如，数组排序之后为{1,1,3,4,5}，在1和3之间空缺了一个2，刚好我们有一个0，可以把它当做2去填补这个空缺。
    于是我们需要做3件事情：
        ①把数组排序
        ②统计数组中0的个数
        ③统计排序之后数组中相邻数字之间的空缺总数
        
    另外：如果数组中的非0数字重复出现，则该数组不是连续的
'''
import random


def isContinuous(nums, k):  # nums 是扑克牌的所有牌  ， k是选取几张牌
    data = [random.choice(nums) for _ in range(k)]
    print "data:", data
    data.sort()
    zero_count = data.count(0)
    small = zero_count
    big = small + 1

    numberOfGap = 0
    while big < k:
        if data[small] == data[big]:
            return False
        numberOfGap += data[big] - data[small] - 1
        small = big
        big += 1

    return numberOfGap == zero_count


nums = [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
        9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
# print len(nums)
for i in range(100):
    print "i:", i
    ret = isContinuous(nums, 5)
    print "ret:", ret
    print "--------------\n"
    if ret is True:
        break

