# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/21 下午5:16
 @desc:
"""
'''
题目：定义一个函数，在该函数中可以实现任意两个整数的加法。由于没有限定输入两个数的大小范围。我们也要把它当做大数问题来处理。
     在Q12第一个思路中，实现了在字符串表示的数字上加1的功能，我们可以参考这个思路实现两个数字的相加功能。另外还需要注意的
     问题：如果输入的数字中有负数，我们应该怎么去处理。
'''

'''
解析；
     
'''

def big_number_add(number1, number2):
    number1_list = list(number1)
    number2_list = list(number2)

    lenght1 = len(number1_list)
    lenght2 = len(number2_list)
    if lenght1 > lenght2:
        for i in range(lenght1-lenght2):
            number2_list.insert(0, '0')
    else:
        for i in range(lenght2-lenght1):
            number1_list.insert(0, '0')
    maxLength = len(number1_list)
    result = ['0'] * maxLength

    iSum = 0
    carryBit = 0
    for i in xrange(maxLength-1, -1, -1):
        a = ord(number1_list[i])
        b = ord(number2_list[i])
        iSum = ord(number1_list[i]) + ord(number2_list[i]) - 2*ord('0') + carryBit

        if iSum >= 10:
            iSum -= 10
            carryBit = 1
            result[i] = chr(ord('0') + iSum)
        else:
            carryBit = 0
            result[i] = chr(ord('0') + iSum)

    if carryBit == 1:
        result.insert(0, '1')

    print ''.join(result)




big_number_add('92147569321', '8026357410')




