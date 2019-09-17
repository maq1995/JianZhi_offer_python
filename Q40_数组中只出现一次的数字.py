# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/16 下午4:58
 @desc:
"""
'''
题目：一个整型数组中除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字，自求时间复杂度为O(n),空间
     复杂度为O(1).
    例如输入数组{2,4,3,6,3,2,5,5}，只有4和6两个数字只出现了一次，其他数字都出现了两次，所以庶出和6
     
解析：
    这个题目比较难。
    首先考虑这个数组中只有一个数字只出现一次，其他的都出现了两次，怎么找出这个数字？
    我们想到异或运算的一个性质，任何一个数字异或它自己都等于0，也就是说，如果我们从头到尾依次异或数组中的每一个数字，那么最终的
结果刚好是哪个只出现了一次的数字，因为那些成对出现的数字都在异或中抵消了。
    下面再考虑原始问题，看看能不能运用相同的思路。我们试着把原数组分为两个子数组，使得每个子数组包含一个只出现一次的数字，而其他
数字都成对出现两次。
    我们还是从头到尾依次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果，该结果肯定不是0，也就是说，
该抑或结果的二进制表示中至少有一位是1，我们在结果数字中找到第一个为1的位的位置，记为第n位。现在我们以第n位是不是1为标准把原数组
中的数字分为两个子数组，第一个子数组中每个数字的第n位都是1，第二个子数组中的每个数字的第n位都是0，那么出现了两次的数字肯定被分配
到同一个子数组中，因为两个相同的数字的任意一位都是相同的。于是我们已经把原数组分成了两个子数组，每个子数组都包含一个只出现一次的
数字，而其他数字都出现了两次。 
'''


# # 数组中只有1个数字只出现了1次，其他数字都出现了两次
# def one_number_once(array):
#     if not array:
#         return None
#     temp = 0
#     for n in array:
#         temp ^= n
#     print temp
#
#
# arr = [2, 3, 4, 5, 2, 3, 4]
# one_number_once(arr)


def two_numbers_once(array):
    if not array:
        return None
    temp = 0
    for n in array:
        temp ^= n
    # 得到第一个1
    ret = 0
    while temp & 1 == 0 and ret < 32:
        temp = temp >> 1
        ret += 1

    a_ret, b_ret = 0, 0
    for n in array:
        if is_one(n, ret):
            a_ret ^= n
        else:
            b_ret ^= n

    return a_ret, b_ret


def is_one(num, t):  # 验证t位是不是1
    num = num >> t
    return num & 0x01


arr = [2, 4, 3, 6, 3, 2, 5, 5]
print two_numbers_once(arr)