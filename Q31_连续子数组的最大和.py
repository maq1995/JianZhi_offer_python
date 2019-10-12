# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/11 下午5:34
 @desc:
"""
'''
题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
     例如输入的数组为{1， -2， 3， 10， -4， 7， 2， -5}，和最大的子数组为{3， 10， -4， 7， 2}， 和为18.
'''

'''
解法1：我们试着从头到尾逐个累加示例数组中的每个数字。
    首先，初始化和为0，
    第一步，加上第一个数字1，此时和为1， 最大和为1
    第二步，加上第二个数字-1， 此时和为-1， 最大和不变，仍然为1
    第三步，加上第三个数字3，因为当前的和为-1，如果用3加上-1，那么和为2，比3本身还要小。也就是说从第一个数字开始的子数
           组的和肯定小于从第三个数字开始的子数组的和。因此我们不用考虑从第一个数字开始的子数组，之前的和也被抛弃。
           所以，此时和为3， 最大和更新为3
    第四步，加上第四个数字10，此时和为13， 最大和更新为13
    第五步，加上第五个数字-4，此时和为9，最大和为13
    第六步，加上第六个数字7，和为16，最大和更新为16
    第七步，加上第七个数字2，和为18， 最大和更新为18
    第八步，加上第八个数字-5，和为13，最大和为18
    数组遍历完毕，结果：最大和为18
'''


def FindGreatestSumOfSubArray(array):
    if not array or len(array) <= 0:
        return None
    sum = 0
    max_sum_of_sub_array = float('-inf')
    for i in array:
        if sum <= 0:
            sum = i
        else:
            sum += i
            if sum > max_sum_of_sub_array:
                max_sum_of_sub_array = sum

    return max_sum_of_sub_array,


# arr = [1, -2, 3, 10, -4, 7, -2, -5]
# sum = FindGreatestSumOfSubArray(arr)
# print sum



'''
解法2：动态规划法
    如果使用函数f(i)表示以第i个数字结尾的子数组的最大和，那么我们需要求出max[f(i)],其中0<=i<=n,我们可以使用如下递归公式求f(i)
           |  data[i]   当i=0或f(i-1)<=0
    f(i) = |
           |  f(i-1) + data[i]  当i！=0并且f(i-1)>0
           
    这个公式的意义：当以第i-1个数字结尾的子数组中所有数字的和小于0时，如果把这个负数与第i个数字相加，得到的结果比第i个数字本身
还要小，所以这种情况下以第i个数字结尾的子数组就是第i个数字本身。如果以第i-1个数字结尾的子数组中所有数字的和大于0，与第i个数字
相加就能得到以第i个数字结尾的子数组中所有数字的和。
    
    
    # 动态规划法
        # f(i)表示以第i个数字结尾的子数组的所有数字的和。
        # 当以第i-1个数字结尾的子数组的所有数字的和小于0时， f(i) = f(i-1) + array[i] 一定小于array[i]
        # 所以这种情况下，以第i个数字结尾的具有最大和的子数组是array[i]自己
        # 当以第i-1个数字结尾的子数组的所有数字的和大于0时，f(i) = f(i-1) + array[i] 一定大于array[i]
        # 多以这种情况下，以第i个数字结尾的具有最大和的子数组是array[0],array[1],...array[i-1],array[i]
        
        
    使用循环代码与解法1的代码一致。
'''


def max_sum_of_ub_array(array):
    if not array or len(array)<=0:
        return None
    max_sum = float('-inf')

    sum = 0
    for i in array:
        if sum <= 0:
            sum = i
        else:
            sum += i
        max_sum = max(max_sum, sum)
    return max_sum

