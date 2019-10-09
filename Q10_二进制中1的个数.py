# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/20 下午4:57
 @desc:
"""
'''
二进制的位运算：
    位运算只有5中：与、或、异或、左移、右移

左移：
    左移运算符 m << n 表示把m向左移n位。左移n位时，最左边的n位将被丢弃，同时在最右边补上n个0
右移：
    右移运算符 m >> n 表示把m向右移n为。右移n位时，最右边的n位将被丢弃，
                                                    如果该数为无符号数，则用0填充最左边的n位；
                                                    如果该数是有符号数值，则用符号位填充最左边的n位。 
    简而言之就是，在右移操作中，使用符号位填充左边空出来的位置。

注意: 在Python中，&表示位运算， and 表示逻辑运算与
    即  2&1 = 0  
    而 a and b ，短路效应，当a为False时，b不会被判断，直接返回a,当a为True时，表达式的值就取决于b，所以返回b.
            False and 1 = False     
            0 and 1 = 0
            []  and 1 = []
            2 and 1000 = 1000
'''

'''
题目： 请事先一个函数，输入一个整数，输出该数二进制表示中1的个数。
     例如把9表示为二进制是1001，有2个是1，所以如果输入是9， 该函数输出2

解析：（自己首先想到的是转换为二进制，在转换过程中统计1的个数，忽略了移位运算， 4>>1 = 2,  2>>1 = 1）
    首先我们想到的是：利用右移操作统计整数的二进制中1的个数,判断该数的最后一位是不是1，接着将输入的数右移移位，继续判断.
                   但是，使用右移操作时，当输入的数是负数时，最左边的填充都是1，最终，移位之后的数会变成11111111，陷入死循环。
    
    为了避免陷入死循环，我们不用右移，改为使用左移。
    左移操作：此时，我们不再是对操作数进行移位，
            首先将操作数与1进行与操作，判断最后一位数是不是1
            然后将1左移1位 变为2， 将操作数与2进行与操作，判断倒数第二位是不是1
            ...
            以此类推
    但是此方法编程不太好
    
最终解法：
        在分析这种解法之前，我们先来分析把一个数减去1的情况。
        如果一个整数不等于0，那么该整数的二进制表示中至少有一位是1,。先假设这个数的最右边一位是1，那么减去1后，最后一位变成0
    而其他位保持不变。也就是相当于最后一位做了取反操作
        接下来假设最后一位不是1而是0的情况。如果该整数的二进制表示中最右边的1位于第m位，那么减去1后，第m位变为0，而第m位之后的
    所有0变为1，第m位之前的所有为保持不变。例如：1100，它的最右边的1是位于索引为2处，减去1之后变为1011.
        在前面的两种情况中，我们发现把一个整数减去1，都是吧最右边的1变成0，如果它的右边还有0的话，就把所有的0变成1，而它左边的
    所有位保持不变。
        接着我们把一个整数和它减去1的结果做位与运算，结果就相当于把最右边的1变成0，其他位保持不变.例如：二进制1100，减去1的结果
    为1011，然后1100 和1011 做位与运算得到的结果为1000.
    
        总结一下就是：把一个整数减去1，再和原整数做位与运算，会将该整数的最右边的1变为0.
         
'''


#  右移  pass
def number_of_1_right_move(n):
    count = 0
    while n != 0:
        if n & 1 != 0:  # 判断最后一位是不是1
            count += 1
        n = n >> 1
    return count


#  右移  pass
def number_of_1_right_move_improved(n):
    count = 0
    if n < 0:
        n = n & 0xffffffff
    while n != 0:
        if n & 1 != 0:  # 判断最后一位是不是1
            count += 1
        n = n >> 1
    return count

# print number_of_1_right_move(-1)
# print number_of_1_right_move_improved(-1)


# 左移
def number_of_1_left_move(n):
    count = 0
    flag = 1
    if n < 0:
        n = n & 0xffffffff
    while flag:  # ？？？？？？？？？？？
        if n & flag != 0:
            count += 1
        flag = flag << 1
    return count


# print number_of_1_left_move(1)


def numbr_of_1_final(n):
    count = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        count += 1
        n = n & (n-1)
    return count


print numbr_of_1_final(1)
