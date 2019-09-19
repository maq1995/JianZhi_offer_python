# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/17 下午3:20
 @desc:
"""
'''
题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率

'''

'''
解法1：基于递归求骰子点数
    要想求出n个骰子的点数和，可以先把n个骰子分为两堆：第一堆只有一个，另一个有n-1个。单独的那一个有可能出现从1到6的点数，我们
需要计算从1到6的每一种点数和剩下的n-1个骰子来计算点数和。接下来把剩下的n-1个骰子还是分成两堆，第一堆只有一个，第二堆有n-2个，
我们把上一轮哪个单独骰子的点数和这一轮单独骰子的点数相加，再和剩下的n-2个骰子来计算点数和。
    可以发现这是一个递归的思路，递归结束的条件就是最后只剩下一个骰子。
    用f(n)表示n个骰子出现的点数，则f(n) = f(n-1)  + f(n-2) + .... + f(1)
'''


def printProbability(number):
    if number < 1:
        return None
    maxSum = number * 6
    pProbability = []
    for i in range(0, 6*number-number+1+1):
        pProbability.append(0)

    Probability(number, pProbability)

    total = 6**number
    for i in range(number, maxSum+1):
        ratio = float(pProbability[i-number]) / total
        print "sum:", i, "ratio:", ratio


def Probability(number, pProbability):
    for i in range(1, 6+1):
        ProbabilityCore(number,  number, i, pProbability)


def ProbabilityCore(original, current, sum, pProbability):
    if current == 1:
        pProbability[sum-original] += 1
    else:
        for i in range(1, 6+1):
            ProbabilityCore(original, current-1, i+sum, pProbability)


# printProbability(2)


'''
解法2：
    基于循环求骰子点数
    我们可以考虑使用两个数组来存储骰子点数的每一个总数出现的次数。在一次循环中，第一个数组中的第n个数字表示骰子和为n出现的次数。
在下一次循环中，我们加上一个新的骰子，此时和为n的骰子出现的次数应该等于上一次循环中骰子点数和为n-1,n-2,n-3,n-4,n-5,n-6的次数
的总和，所以我们把另一个数组的第n个数字设为前一个数组对应的第n-1,n-2,n-3,n-4,n-5,n-6之和。
'''
import numpy as np


def get_probability(n):
    if n < 1:
        return []
    pProbability = np.zeros(shape=[2, 6*n+1])

    flag = 0
    for i in range(1, 7):
        pProbability[flag][i] = 1

    for k in range(2, n+1):
        for i in range(0, k):
            pProbability[1-flag][i] = 0
        for i in range(k, 6*k+1):
            pProbability[1-flag][i] = 0
            j = 1
            while j <= i and j <= 6:
                pProbability[1-flag][i] += pProbability[flag][i-j]
                j += 1

        flag = 1 - flag

        total = 6 ** n
        for i in range(n, 6*n+1):
            ratio = float(pProbability[flag][i]) / total
            print "sum:", i, "ratio:", ratio


get_probability(2)