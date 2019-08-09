# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/9 上午8:50
 @desc:题目：有两个排序的数组A1和A2，内存在A1的末尾有足够多的空余空间容纳A2.请实现一个函数，把A2中的所有数字插入到A1中并且所有数字
 都是排序的。
"""
import numpy as np
'''
分析：
    本题的关键是在A1上进行扩展，不能创建新的数组。
思路：
    如果可以创建新的数组的话，实现就比较简单。
    但是本题要求在A1上进行扩展，所以与Q4_替换空格一样，需要先计算出最终数组的长度，然后从后向前进行数组A1和A2的元素比较，
并将元素放在相应的位置。（可以这样做的前提：A1和A2是已经有序的！！！）
'''
'''
总结：
    ！！合并！！两个数组、字符串的，如果从前向后复制每个数字、字符需要重复移动数字、字符多次、那么我们可以考虑从后向前
复制，这样可以减少移动的次数，从而提高效率。
'''


def merge_arrars(a, b):
    if a is None and b is None:
        return None
    elif a is None:
        return b
    elif b is None:
        return a
    else:
        l1 = len(a)
        l2 = len(b)
        i = l1 + l2 - 1
        a = np.concatenate((a, np.zeros(shape=(l2,))), axis=0)
        # print 'a:', a
        while i >= 0 and l1 != 0 and l2 != 0:
            if a[l1 - 1] <= b[l2 - 1]:
                # a = np.insert(a, i, b[l2-1], axis=0)  # np.inster会自动填充一个新的位置，使得数组长度+1
                a[i] = b[l2-1]
                i -= 1
                l2 -= 1
            else:
                a[i] = a[l1-1]
                # a = np.insert(a, i, a[l1-1], axis=0)
                i -= 1
                l1 -= 1
        if l1 == 0:
            a[:i+1] = b[:l2]

        return a


a = np.array([1, 2, 6])
b = np.array([12, 77, 89])
print merge_arrars(a, b)

