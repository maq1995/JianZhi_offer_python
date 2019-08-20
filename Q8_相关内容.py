# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2
 @time: 2019/8/19 下午4:52
 @desc:
"""
'''
不管是用循环还是递归，买面试官都期待应聘者能够信手拈来写出完整正确的二分查找代码
'''


# 循环 二分查找
def binary_search_xh(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == num:
            print "found it!"
            return
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    print "Failed!"
    return


# array = [2, 3, 4, 8, 9, 15, 16, 22, 30]
# binary_search_xh(array, 30)


# 递归  二分查找
def binary_search_dg(arr, num, low, high):
    mid = (low + high) / 2
    if low <= high:
        if arr[mid] == num:
            print "found it!"
            return
        elif arr[mid] < num:
            return binary_search_dg(arr, num, mid+1, high)
        else:
            return binary_search_dg(arr, num, low, mid-1)

    print "Failed!"
    return


# array = [2, 3, 4, 8, 9, 15, 16, 22, 30]
# binary_search_dg(array, 30, 0, len(array)-1)


'''
很多公司的面试官喜欢在面试环节中要求应聘者写出快速排序的代码
实现快速排序算法的关键在于：
先在数组中选择一个数字，接下来把数组中的柱子分为两部分，比选择的数字小的移到数字的左边，比选择的数字大的移到数字的右边
'''


# 第一种实现：经典的  使用两个指针

# 一趟快速排序
def partition(arr, left, right):
    key = arr[left]
    while left < right:
        while right > left and arr[right] >= key:
            right -= 1
        if left < right:
            arr[left] = arr[right]
            left += 1

        while left < right and arr[left] < key:
            left += 1
        if left < right:
            arr[right] = arr[left]
            right -= 1

    arr[right] = key
    print arr
    return left


def quick_sort_1(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quick_sort_1(arr, start, p-1)
        quick_sort_1(arr, p+1, end)
    return


# nums = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
# quick_sort_1(nums, 0, len(nums)-1)


# 插入排序 ： 插入排序与我们打扑克时整理手上的牌非常类似
# 通过构建有序序列（我们去取数组第一个元素作为有序序列），对于未排序数据，在已排序序列中从后向前扫描，找到相应的位置并插入。
# 注意：不开辟新的数组空间，   插入排序是在无序数组基础上进行排序
def insert_sort(arr):
    for i in range(1, len(arr)):
        # 与有序数列逆序对比
        temp = arr[i]
        l = 0
        for j in range(i-1, -1, -1):
            if arr[j] > temp:
                arr[j+1] = arr[j]
            else:
                l = j+1
                break
        arr[l] = temp
        print arr
    return


# arr = [6, 1, 7, 5, 8, 2, 3, 4]
# insert_sort(arr)


# 冒泡排序 ：
# 从第一个开始每次都比较相邻的两个数，如果发现顺序不对，就把两个数交换一下，直到最后一个。
# 这个时候，最大的数自然而然就跑到最后一位上面去了。
#
# 第二次的时候，也从第一个开始，不过只需要循环到n-2处就行了（因为n-1处经过第一次洗礼已经时最大了嘛。）
#
# 。。。。。。依此类推，循环n次，整个数组就会变成有序的了。
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
        print arr


# arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubble_sort(arr)


# 选择排序——简单粗暴的排序
# 在第一次遍历中，从最开始到最后。找到最大/最小的数，并于最后一个/第一个交换。
#
# 在第二次中，从最开始到倒数第二个。找到最大/最小的数，并于倒数第二个/正数第二个交换。
#
# 。。。。以此类推，循环n次。完成没有任何技术含量，所以效率几乎也是所有排序中最低的，强烈不推荐。
def select_sort(arr):
    for i in range(len(arr)):
        flag = i
        for j in range(i, len(arr)):
            if arr[j] < arr[flag]:
                flag = j
        arr[flag], arr[i] = arr[i], arr[flag]
        print arr


# arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# select_sort(arr)


# 归并排序 ：利用分治思想实现的排序，也是一种效率很高的排序
# 在归并排序的时候，我们将数组不断的拆分为两半，直到数据只剩一个的时候，然后再按照大小顺序把他们拼装起来。
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) / 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# 合并两个有序数组
def merge(left, right):
    temp = []
    left_p, right_p = 0, 0
    while left_p < len(left) and right_p < len(right):
        if left[left_p] <= right[right_p]:
            temp.append(left[left_p])
            left_p += 1
        else:
            temp.append(right[right_p])
            right_p += 1
    if left_p != len(left):
        # temp.append(left[left_p:])
        temp += left[left_p:]

    if right_p != len(right):
        # temp.append(right[right_p:])
        temp += right[right_p:]
    print "temp:", temp
    return temp


# arr = [6, 5, 3, 7, 2, 8, 1, 6]
# merge_sort(arr)

'''
对比插入排序、冒泡排序、归并排序、快速排序、选择排序的优劣。（额外空间消耗、平均时间复杂度、最差时间复杂度）
'''
'''
|--算法--|--平均时间复杂度--|--最差时间复杂度--|--额外空间消耗--|--稳定度--|
|--------|---------------|----------------|--------------|---------|
 冒泡排序     O(n^2)            O(n^2)            O(1)        稳定
 选择排序     O(n^2)            O(n^2)            O(1)        稳定 （排序前后两个相等的数相对位置不变，则算法稳定）
 插入排序     O(n^2)            O(n^2)            O(1)        稳定
 快速排序     O(nlogn)          O(n^2)            O(logn)-O(n) 不稳定
 归并排序     O(nlogn)          O(nlogn)          O(n)          稳定
'''



