# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/12 上午11:00
 @desc:
"""
'''
题目：输入一个正整数数组，把数组中所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
    例如输入数组为{3， 32， 321}，则打印出这3个数字能排成的最小数字321323.
    
解析：
    这道题其实是希望我们能找到一个排序规则。数组根据这个规则排序之后能排成一个最小的数字。要确定排序规则，就要比较两个
数字，也就是说给出两个数字m和n。我们需要确定一个规则判断m和n哪个应该排在前面，而不仅仅比较这两个数字的值哪个更大。
    根据题目的要求，两个数字m和n能拼接成数字mn和nm。如果mn<nm那么我们应该打印mn,也就是m应该排在n的前面。我们定义
此时m“小于”n；反之，如果nm<mn，则定义n"小于"m，如果mn=nm,则定义m"等于"n.
    接下来我们考虑怎么去拼接数字，即给出数字m和n,怎么得到mn和nm并比较它们的大小，直接用数字计算不难办到，但是应该考虑到
一个潜在的问题是m和n都在int范围内，但是它们拼接起来的数字mn或nm可能会超出int的表示范围。所以这还是一个隐形的大数问题。
    一个直观的解决大数问题的方法就是把数字转换成字符串。另外，由于数字m和n拼接起来得到的mn和nm的位数是相同的，因此比较
它们的大小只需要按照字符串大小的比较规则就可以了。
'''


def printMinNumber(array):
    if not array or len(array) <= 0:
        print None
        return

    m = str(array[0])
    for n in range(1, len(array)):
        minus = int(str(array[n]) + str(m)) - int(str(m) + str(array[n]))
        if minus <= 0:
            m = str(array[n]) + str(m)
        else:
            m = str(m) + str(array[n])
    print m
    return


arr = [3, 32, 321]
printMinNumber(arr)






