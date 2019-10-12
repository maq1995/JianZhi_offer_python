# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/12 上午9:44
 @desc:
"""
'''
题目：输入一个整数n,求从1到n这n个整数的十进制表示中1出现的次数。
     例如输入12，从1到12这些整数中包含1的数字有1， 10， 11和12， 1一共出现了5次
'''

'''
解析：
      1位数，1-9中，1一共出现了1次；

      2位数，10-99中，10-19的十位上一共出现了10*1=10次，
            对于每个十位开头的数字10-19、20-29，每个数个位上出现的是1-9，所以对于每个区间1出现的次数为1，共有9个区间。9*1=9
            1一共出现了：10 + 9*1= 19
            
      3位数，100-999，100-199百位上出现了10**2=100次，
            对于每个百位数开头，例如100-199，200-299，低位上其实就是0-99这个区间上1出现的次数，一共9个区间 9*19=171次
            1一共出现了100 + 9*19 = 271
            
    所以：对于1-9， 10-99， 100-999，每个n位数中包含1的个数的公式为：
    f(x): x 表示x位数
    f(1) = 1 = 10^0
    f(2) = 10^(2-1) + 9 * f(1) = 19
    f(3) = 10^(3-1) + 9 * f(2) = 171
    ...
    f(n) = 10^(n-1) + 9 * f(n-1)
    
    但是这个规律要求输入的数字必须是x位数中最大的数。比如输入的数字为9， 99， 999等，但是当输入的数字为235， 1586时，还
需要做进一步处理。
     例如输入的式子为23456，我们可以用上述公式求出1-9999中共出现的1的次数，接下来需要求10000-23456之间出现的1个次数。
     
     首先看输入的数最高位的数字，然后看低位的数字
        1.如果最高位为1，比如输入的数为1234， 我们首先求出了1-999之间1出现的次数，下面要求1000-1234之间1出现的次数，因为输
          入的数字1234最高位为1，则最高位上1出现的次数为234+1=235个；
          低位数字剩余的234， 接下来可以使用递归的方式求解：最高位2，
        2.如果最高位大于1，比如输入的数为34567，我们首先求出来1-9999之间1出现的次数，下面要求10000-34567之间1出现的次数，
          因为最高位为3，大于1，则最高位出现1的是在区间10000-19999中（20000-29999的最高位没有出现过1）,一共10^4个，
          然后因为10000-19999和20000-29999中的低位满足上面的f(n)的表达式，所以可以直接使用公式求解。
          剩余的30000-34567，低位数字为4567， 递归解决：最高位4，大于1，首先求出1000-3999之间1出现的次数，剩余4000-4567，
          再递归即可。
     
'''


# 计算数字nums是几位数
def get_weishu(nums):
    ret = 0
    while nums:
        ret += 1
        nums /= 10

    return ret


# 计算整位数（1-9， 10-99， 100-999）之间1出现的次数
def get_nums_of_1_in_right_weishu(n):  # n表示位数
    if n <= 0:
        return 0
    if n == 1:
        return 1
    current = 9 * get_nums_of_1_in_right_weishu(n-1) + 10**(n-1)

    return current


# 主要部分
def get_1_nums(nums):  # nums:是一个数
    if nums < 10:
        return 1 if nums >= 1 else 0
    # 获得数字nums是几位数
    digit = get_weishu(nums)

    # 计算数字之前整位数中1出现的次数，所以要digit-1
    low_right_weishu_count = get_nums_of_1_in_right_weishu(digit-1)

    # 首先看最高位的数字
    high = int(str(nums)[0])  # 得到最高位的数字
    low = nums - high * 10**(digit-1)
    if high == 1:
        high_count = low + 1
    else:
        high_count = 10**(digit-1)  # 1xxx- 1999..之间最高位上1出现的次数
        high_count += get_nums_of_1_in_right_weishu(digit-1) * (high-1)

    low_count = get_1_nums(low)

    return low_right_weishu_count + high_count + low_count


n = 101
print get_1_nums(n)

"""
解法2：更简单易懂：https://blog.csdn.net/maqian5/article/details/102517534

"""
def NumberOf1Between1AndN_Solution(n):
    if n <= 0:
        return 0

    round = n
    count = 0
    base = 1
    while round != 0:
        weight = round % 10
        round = round / 10
        count += round*base
        if weight > 1:
            count += base
        elif weight == 1:
            count += (n % base) + 1
        base = 10 * base


    return count

