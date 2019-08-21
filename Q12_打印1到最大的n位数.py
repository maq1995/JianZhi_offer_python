# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/21 上午10:21
 @desc:
"""
"""
题目：输入数字n,按顺序打印出从1到最大的n位十进制数。比如输入3，则打印出1、2、3、、、999.

解析：
    我们可以看出，题目中并没有规定n的范围。当输入的n很大时，我们要求最大的n位数会不会用整型或者是长整型都会溢出？所以如果直接
用一个循环，从1开始打印的话，会出现问题。
    也就是说，我们需要考虑！！！大数问题！！！
"""
"""
    解法1：使用字符串或者数组表达大数，前面的部分表示高位，后面的部分表示低位。
          首先，把字符串中的每一个数字都初始化为‘0’，然后，每一次为字符串表示的数字加1，再打印出来。
          问题①：如何在字符串表达的数字上模拟加法？
          解答：每次在字符串表示的大数最后一个索引处加上1，再判断需不需要进位
          问题②：如何判断是否已经达到了n位数最大的数？
          解答：在第一个索引处产生进位时，就说明已经是最大的n位数了
          问题③：如何打印字符串表示的数字？
          解答：正序遍历字符串，当遇到第一个不是‘0’的字符时开始打印，知道字符串的结尾。   
"""


# 解法1
def print_1_to_max_of_n_digits(n):
    if n <= 0:
        return
    str = '0' * n
    numbers = list(str)
    while Increment(numbers) is False:
        printNumber(numbers)


def Increment(numbers):
    isOverFlow = False
    nTakeOver = 0  # 记录进位
    nLength = len(numbers)

    for i in xrange(nLength-1, -1, -1):
        nSum = ord(numbers[i]) - ord('0') + nTakeOver
        if i == nLength - 1:
            nSum += 1

        if nSum >= 10:
            if i == 0:
                isOverFlow = True
            else:
                nSum -= 10
                nTakeOver = 1
                numbers[i] = chr(ord('0') + nSum)
        else:
            numbers[i] = chr(ord('0') + nSum)
            break

    return isOverFlow


def printNumber(numbers):
    isBegining0 = True
    nLenght = len(numbers)

    for i in xrange(0, nLenght):
        if isBegining0 is True and numbers[i] != '0':
            isBegining0 = False
        if isBegining0 is False:
            print ''.join(numbers[i:])
            break


# print_1_to_max_of_n_digits(2)


'''
解法2：
    上面的思路比较直观，但是对于面试来说代码量有点多。我们可以换一种思路来解决这个问题。
    如果在数字前面补0的话，就会发现n位所有十进制数其实就是n个从0到9的全排列。也就是说，我们把数字的每一位都从0到9排列一遍，
就得到了所有的十进制数。只是我们在打印的时候，数字排在前面的0我们就不打印出来。
    全排列用递归很容易表达，数字的每一位都可能是0-9之间的一个数，然后设置下一位，递归结束的条件是我们已经设置了数字的最后一位.
'''


def print_1_max_of_n_digits_dg(n):
    if n <= 0:
        return
    number = ['0'] * n
    for i in range(10):
        number[0] = str(i)
        pint1ToMaxOfDigitsRecursively(number, n, 0)


def pint1ToMaxOfDigitsRecursively(number, legth, index):
    if index == legth-1:
        print_number(number)
        return
    for i in range(10):
        number[index+1] = str(i)
        pint1ToMaxOfDigitsRecursively(number, legth, index+1)


def print_number(number):
    isBegining0 = True
    nLength = len(number)

    for i in range(nLength):
        if isBegining0 is True and number[i] != '0':
            isBegining0 = False
        if isBegining0 is False:
            print ''.join(number[i:])
            break


print_1_max_of_n_digits_dg(2)