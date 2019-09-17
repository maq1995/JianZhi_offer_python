# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/16 下午7:12
 @desc:
"""
'''
题目1：输入一个递增排序的数组和数字s，在数组中查找两个数，使得它们的和正好是s，如果有多对数字的和等于s,输出任意一对即可。
     例如：数组为{1,2,4,7,11,15},s为15，则输出的为4和11
     
解析：
    暴力法，略过
    因为题目中说数组是递增排序的，所以我们应该好好利用这个性质。
    我们先在数组中选择两个数字，如果它们的和等于s，我们找到了要找的数字，如果和小于s呢？我么希望两个数字的和再大一点，由于数组
已经排好序了，我们可以考虑选择较小的数字后面的数字。如果和大于s，我们可以考虑较大数字前面的数字。
    以题目中例子为例，解释这个过程：定义两个指针，第一个指针指向数组第一个（最小的）数字1，第二个指针指向数组最后一个（最
大的）数字15，1+15=16， 16>15，所以我们将第二个指针向前移动，指向11，此时1+11=12，12<15,则将第一个指针向后移动，指向2,
2+11=13, 13<15,接着将第一个指针向后移动，指向4,4+11=15，找到！！！
'''


def FindNumbersWithSum(array, s):
    if not array:
        return None
    head, end = 0, len(array)-1
    while head < end:
        if array[head] + array[end] == s:
            return array[head], array[end]
        elif array[head] + array[end] > s:
            end -= 1
        else:
            head += 1

    return None


array = [1, 2, 4, 7, 11, 15]
s = 7
# print FindNumbersWithSum(array, s)


'''
题目2：输入一个正数s，打印出所有和为s的连续正数序列（至少包含两个数）。例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，
     所以结果打印出3个连续序列：1,2,3,4,5  和   4,5,6  和7,8.
     
解析：
    有了解决前面问题的经验，我们考虑用两个数small和big分别表示序列的最小值和最大值。首先将small初始化为1，big初始化为2，
如果small到big的序列和大于s，我们就从序列中去掉较小的值，也就是增大small的值，如果small到big的序列和小于s,那么就增大big，
使得序列包含更多的数字，因为这个序列至少要有两个数字，我们一直增加small到（1+s）/2为止。 
    以求和为15的所有连续序列为例（1+15）/2=8，我们先把small初始化为1，big初始化我2，此时small和big之间的序列是{1,2}，和为3小于15，将
big增大，指向3，此时序列为{1,2,3}，和为6，小于15，继续增大big,序列为{1,2,3,4}和为10，小于15，增大big,此时序列为{1,2,3,4,5}，
和为15，输出序列；   接下来再增大big,序列为{1,2,3,4,5,6}，和为21，大于15，则增大small，序列为{2,3,4,5,6}，和为20，大于15，
继续增大small，序列为{3,4,5,6}，和为18，大于15，增大small，序列为{4,5,6}， 和为15，输出序列；    接下来再增大small（？），
序列为{5,6}，和为11，小于15，增大big, 序列为{5,6,7}，和为18，增大small， 序列为{6,7}，和为13，小于15，增大big,序列为{6,7,8}，
和为21，大于15，增大small，序列为{7,8}，和为15，输出序列；    继续增大small，序列为{8}，和为8， 小于15，增大big, 序列为{8,9}
和为17， 大于15， 增大small，但是small再增加就超过了（1+s）/2,则停止。
'''


def FindContinuousSequence(s):
    if s < 3:
        return None
    ret = []
    small = 1
    big = 2
    mid = (1 + s) / 2

    while small < mid:
        if sum(range(small, big+1)) == s:
            ret.append(range(small, big+1))
            big += 1  # small += 1 也可以
        elif sum(range(small, big+1)) > s:
            small += 1
        else:
            big += 1

    return ret


s = 4
print FindContinuousSequence(s)
