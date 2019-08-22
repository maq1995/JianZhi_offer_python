# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/22 上午8:41
 @desc:
"""
'''
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分

解析：
    暴力方法：从头扫描整个数组，当碰到一个偶数时，拿出这个数字，将位于这个数字后面的所有数字向前挪动一位，这样末尾会有一个空位，
            此时，将该数字放入到这个空位中；当碰到一个奇数时，可以不用管。但是这样的时间复杂度为O(n^2)
            
    指针方法：
            这个题目要求奇数放在数组的前半部分，偶数放在数组的后半部分，因此所有的奇数应该位于偶数的前面。也就是说我们在扫描整个
            数组的时候，如果发现偶数在奇数的前面，交换它们即可。
            所以我们维护两个指针，第一个指向数组的开头，它只向后面移动，第二个指向数组的结尾，它只向前面移动，在两个指针相遇之前，
            第一个指针向后移动，如果遇到一个偶数，再将第二个指针向前移动，直到遇到一个奇数，那么交换两个数，否则，继续移动指针即可；
            当两个指针相遇之后（第二个指针位于第一个指针前面），算法结束
        
    可扩展方法：
             如果把题目改成把数组中的数按照大小分为两部分，所有负数都在非负数前面，该怎么做？
             如果再把题目改成把数组中的数分为两部分，能被3整除的数都在不能被3整除的数的前面，该怎么做？
             应该可以想到，现在需要提供的不仅仅是解决一个问题的方法，而是解决一系列同类型问题的通用办法。即希望提供一个模式，在
             这个模式下能够很方便的把已有的解决方案扩展到同类型的问题上。
             回到修改的两个问题上，可以看出，需要修改的仅仅是判断是奇数/偶数、负数/非负数、能被3整除/不能被3整除。所以我们可以将
             判断的标准独立出来。然后作为参数传递进入。
             注意！！！函数作为参数传递进另一个函数时，只将函数名传递即可，不用带括号！！！
              
'''


# 指针方法
def reOrrderArray(arr):
    if len(arr) <= 1:
        return arr

    left = 0
    right = len(arr) - 1
    while left <= right:
        while arr[left] & 1 == 1:  # arr[left]是奇数
            left += 1
        while arr[right] & 1 == 0:  # arr[right]是偶数
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    return arr


# arr = [4, 2, 1, 5, 3, 7]
# print reOrrderArray(arr)


# 可扩展方法
def Reorder(arr, function):
    if len(arr) <= 1:
        return arr

    left = 0
    right = len(arr) - 1
    while left <= right:
        while function(arr[left]) is True:
            left += 1
        while function(arr[right]) is False:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    return arr


def isOddNumber(n):
    return n & 1 == 1


def isMinusNumber(n):
    if n < 0:
        return True
    return False

def isDiviveBy3(n):
    if n % 3 == 0:
        return True
    return False


arr = [1, 2, 3, 4, 5, 6, 7]
print Reorder(arr, isOddNumber)
