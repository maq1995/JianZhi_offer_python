# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/16 下午3:16
 @desc:
"""
'''
题目：统计一个数字在排序数组中出现的次数。例如输入排序数组{1,2,3,3,3,3,4,5}和数字3，则输出3出现的次数为4.

解析：
    由于是排序数组，所以很自然地想到使用二分查找法。
    怎么使用二分查找法直接找出第一个k和最后一个k呢？
    
'''


def getFirstK(array, k):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) / 2
        if array[mid] < k:
            if mid + 1 < len(array) - 1 and array[mid + 1] == k:
                return mid + 1
            left = mid + 1
        elif array[mid] > k:
            right = mid - 1
        else:  # array[mid] == k
            if mid - 1 < 0 or (mid - 1 >= 0 and array[mid - 1] < k):
                return mid
            right = mid - 1

    return -1


def getLastK(array, k):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) / 2
        if array[mid] < k:
            left = mid + 1
        elif array[mid] == k:
            if mid + 1 == len(array) or (mid + 1 < len(array) and array[mid + 1] > k):
                return mid
            left = mid + 1
        else:
            if mid - 1 > 0 and array[mid - 1] == k:
                return mid - 1
            right = mid - 1

    return -1


def get_k_counts(array, k):
    if not array:
        return 0
    first = getFirstK(array, k)
    last = getLastK(array, k)

    if first > -1 and last > -1:
        return last - first + 1
    return 0


array = [1, 2, 3, 3, 3, 3, 4, 5]
print get_k_counts(array, 3)
