# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/9 下午4:20
 @desc:
"""
'''
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果，如果是则返回True，否则返回False。
     假设输入数组的任意两个数字都互不相同。
     注意：这里并不给定二叉搜索树，而是判断数组是否符合二叉搜索树的后序遍历的属性。

解析：
    在二叉搜索树的后序遍历中，最后一个数字是根节点的值，数组中前面的数字可以分为两部分，第一部分是左子树结点的值，它们都比根节点的
值小，第二部分是右子树结点的值，它们都比根节点的值大。例如输入数组{5,7,6,9,11,10,8}是某一二叉搜索树的后序遍历，而{7,4,6,5}则不
是某棵二叉搜索树的后续遍历。
    以数组{5,7,6,9,11,10,8}为例，后续遍历结果的最后一个数字8就是根节点的值，在这个数组中，前3个数字5,7,6都比8小，为8的左子树，
后面3个数字9,11,10都比8大，是8的右子树。同样数组{5,7,6}和{9,11,10}也用这个过程判断.这是一个递归的过程。
    以数组{7,4,6,5}为例，最后一个元素5是根节点，由于第一个数字7比5大，因此在对应的二叉搜索树中是没有左子树的，但是右子树中有一个
结点的值4，小于5，不满足二叉搜索树的性质，所以该数组不是某棵二叉搜索树的后续遍历序列。

'''


def is_post_order(post_order):
    if len(post_order) == 0:
        return False
    root = post_order[-1]

    left = 0
    while post_order[left] < root:
        left += 1
    right = left
    while right < len(post_order) - 1:
        if post_order[right] < root:
            return False
        else:
            right += 1

    left_ret = True if left == 0 else is_post_order(post_order[:left])
    right_ret = True if left == right else is_post_order(post_order[left:right])

    return left_ret and right_ret


# list1 = [5, 7, 6, 9, 11, 10, 8]
# list2 = [7, 4, 6, 5]
# print is_post_order(list1)


'''
扩展：输入一个整数数组判断该数组是不是某二叉搜索树的前序遍历的结果。

解析：
    这和前面问题的后续遍历很类似，只是在前序遍历得到的序列中，第一个数字是根节点的值。
'''


def is_pre_order(preOrder):
    if len(preOrder) == 0:
        return False
    if len(preOrder) == 1:
        return True

    root = preOrder[0]

    left = 1
    while preOrder[left] < root:
        left += 1
    right = left
    while right < len(preOrder):
        if preOrder[right] < root:
            return False
        else:
            right += 1

    left_ret = True if left == 1 else is_pre_order(preOrder[1:left])
    right_ret = True if right == left else is_pre_order(preOrder[left:right])

    return left_ret and right_ret


list1 = [8, 6, 5, 7, 10, 9, 11]
list2 = [4, 3, 6, 2]
print is_pre_order(list2)



