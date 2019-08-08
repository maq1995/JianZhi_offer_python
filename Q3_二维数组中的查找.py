# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/8 上午9:13
 @desc: 二维数组中的查找
 题目：  在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
        请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否包含有该整数。
"""
import numpy as np
import numpy

'''
例：
下面的二维数组就是每行每列都递增排序。如果在这个数组中查找数字7，则返回True，如果查找数字5，由于数组中不包含有该数字，则返回False。
1   2   8   9
2   4   9   12
4   7   10  13
6   8   11  15
'''
'''
在解决问题之前，先把测试用例想好，可以提高代码鲁棒性
    1. 数组为空、一维数组、二维数组（但只有一行或一列）， 数字正常   return False
    2. 数组正常， 数字为空、字符串、等  return False
    3. 数组正常， 数字正常：
        A. 数字是数组中的数 : 极大值、极小值、重复数  return True
        B. 数字不是数组中的数 retrun False 
'''

'''
解法1：因为每行每列是有序的，所以暴力搜索的话，就有点对不起这个有序的性质了
所以：
    在分析这个问题的时候，大部分人会将二维数组画成矩形，然后从数组最中间选取一个数字，
    情形.1)如果该数字等于目标查找数字，则直接返回
    情形.2)如果该数字大于目标查找数字，则在当前位置的左边和上边组成的区域进行查找
    情形.3)如果该数字小于目标查找数字，则在当前位置的右边和下边组成的区域查找
    
    问题：如果采用递归的话，剩余的搜索区域不好表示.

'''


# 递归形式  剩余部分不好表示
# 可行方法是：将剩余搜索区域进行拼接成一个新数组，但是这样会有重复的数据，效率降低
# ！！！完成！！！
def two_dimenstion_array_search(array, num):
    print "\n"
    print type(array[0])
    if array is None:
        print "The array is NULL"
        return False
    elif type(array[0]) is not numpy.ndarray:
        print "The array is ileagal"
        return False
    elif not isinstance(num, int):
        print "the number is ileagal"
        return False
    else:
        print "array:", array
        print "len:", len(array)
        print "num:", num
        i = len(array) / 2
        j = len(array[0]) / 2
        print "i:{}, j:{}, array[i][j]:{}".format(i, j, array[i][j])
        if i == 0 or j == 0:
            if num in array:
                print "found it"
                return True
        if array[i][j] == num:
            print "found it!"
            return True
        elif array[i][j] > num:
            # a = array[:i, :j]  # WRONG！ 剩余区域不好表示
            a = array[:i, :]
            b = array[:, :j]
            b = b.T
            c = np.concatenate((a, b), axis=0)
            print "a:", a
            print "b:", b
            print "c:", c
            return two_dimenstion_array_search(c, num)
        else:
            a = array[:i, :]
            b = array[:, :j]
            b = b.T
            c = np.concatenate((a, b), axis=0)
            print "a:", a
            print "b:", b
            print "c:", c
            return two_dimenstion_array_search(c, num)


# 暴力搜索  时间复杂度为o(n^2)   !!!完成!!!
def two_dimenstion_array_search_2(array, num):
    print "\n"
    if len(array) == 0:
        print "The array is ileagal"
        return False
    elif not isinstance(num, int):
        print "the number is ileagal"
        return False
    else:
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == num:
                    print 'found it!'
                    return True

        return False


# # arr = np.array([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])
# n = 4
# arr = np.array([[1], [2], [3], [4]])
# f = two_dimenstion_array_search(arr, n)


'''
书上的解法：
二维数组：1   2   8   9
        2   4   9   12
        4   7   10  13
        6   8   11  15
查找目标：7        
分析：
    之前因为是因为从数组的中间选取一个数来进行比较，所以导致下一次要查找的两个相互重叠的区域；
    那么如果我们从数组的一个角上选取数字，情况会不会变得简单呢？
    
    用上面的例子来看：
    首先我们选取数组的右上角的数字9，因为9>7，所以7不可能出现在9的那一列，所以最后一列可以去掉，现在二维数组变为：
    1   2   8
    2   4   9
    4   7   10
    6   8   11
    再选取右上角的数字8， 因为8>7， 所以7也不可能出现在8这一列，所以将8这一列删掉，现在的二维数组变为：
    1   2
    2   4
    4   7
    6   8
    接着选取右上角数字2，因为2<7，所以7可能出现在下边，但是7不可能出现在2的左边，所以将2所在的行去掉，二维数组变为：
    2   4
    4   7
    6   8
    选取右上角数字4，因为4<7，所以7可能出现在4的下面，不可能出现在4的左边，所以将4所在行删掉，二维数组变为：
    4   7
    6   8
    选取右上角数字7， 7=7，找到！！！
    
感悟：
    选取右上角的位置是至关重要的，对于右上角数字所在的行，其他数字都小于它，对于右上角数字所在的列，其他数字都大于它，所以该位置是
    很重要的。
'''


# 书上的思想， 自己实现的代码
def two_dimenstion_array_search_t(array, num):
    print "\n"
    # print len(array[0])
    if array is None or type(array[0]) is not numpy.ndarray:
        print "The array is illeagal"
        return False
    elif not isinstance(num, int):
        print "the number is illeagal"
        return False
    else:
        print "array:", array
        print "右上角：", array[0][-1]
        if array[0][-1] == num:
            print "found it"
            return True
        elif array[0][-1] < num:
            a = array[1:, :]
            print "in if a:", a
            two_dimenstion_array_search_t(a, num)
        else:
            a = array[:, :len(array[0])-1]
            print "in else a:", a
            two_dimenstion_array_search_t(a, num)


# 书上的代码
def two_dimenstion_array_search_b(array, num):
    if array is None or type(array[0]) is not numpy.ndarray:
        print "The array is illeagal"
        return False
    elif not isinstance(num, int):
        print "the number is illeagal"
        return False
    else:
        row = len(array)
        col = len(array[0])
        i = 0
        j = col-1
        while i < row and j >= 0:
            if array[i][j] == num:
                print 'found it'
                return True
            elif array[i][j] < num:
                i += 1
            else:
                j -= 1
        return False


arr = np.array([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])
n = 4
# arr = np.array([[1], [2], [3], [4]])
f = two_dimenstion_array_search_b(arr, n)
