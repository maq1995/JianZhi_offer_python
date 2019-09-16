# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/16 上午10:19
 @desc:
"""
import copy

'''
题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
    例如在数组{7， 5， 6， 4}中，一共存在5个逆序对，分别是（7， 5）， （7， 6），（7， 4）， （5， 4）， （6， 4）
    

解析：
    具体看书上。
'''


def InversePairs(data):
    if not data:
        return 0

    length = len(data)
    copy = [0] * length
    for i in range(length):
        copy[i] = data[i]

    count = InversePairsCore(data, 0, len(data)-1)
    return count


def InversePairsCore(tmp, start, end):
    if start == end:
        return 0

    mid = (end-start)/2
    left = InversePairsCore(tmp, start, start+mid)
    right = InversePairsCore(tmp, start+mid+1, end)

    count = 0
    # i 初始化为前半段最后一个数字的下标，j初始化为后半段最后一个数字的下标
    i = start + mid
    j = end

    t = []
    while i >= start and j >= start+mid+1:
        if tmp[i] > tmp[j]:
            t.append(tmp[i])
            count = count + (j - start - mid)
            i -= 1
        else:
            t.append(tmp[j])
            j -= 1

    while i >= start:
        t.append(tmp[i])
        i -= 1
    while j >= start+mid+1:
        t.append(tmp[j])
        j -= 1

    tmp[start:end+1] = t[::-1]
    return count + left + right


array = [7, 5, 6, 4, 8, 3]
print InversePairs(array)







