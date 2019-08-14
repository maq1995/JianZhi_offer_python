# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/14 下午3:08
 @desc:
"""
'''
题目：输入某二叉树的前序遍历和中序遍历的结果时，请重建出该二叉树。假设输入的前序遍历和终须遍历中都不包含重复的数字。
例如，前序遍历序列为{1,2,4,7,3,5,6,8}， 中序遍历序列为{4,7,2,1,5,3,8,6}
'''


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def reConstructBinaryTree(pre_list, in_list):
    if not pre_list or not in_list:
        return
    index = in_list.index(pre_list[0])
    left = in_list[0:index]
    right = in_list[index+1:]
    # print "left:", left
    # print "right:", right
    root = TreeNode(pre_list[0])
    root.left = reConstructBinaryTree(pre_list[1:1+len(left)], left)
    root.right = reConstructBinaryTree(pre_list[-len(right):], right)
    return root


pre = [1, 2, 4, 7, 3, 5, 6, 8]
mid = [4, 7, 2, 1, 5, 3, 8, 6]
troot = reConstructBinaryTree(pre, mid)


#  前序遍历 递归版本
def preOrder_digui(t):
    if t is not None:
        print t.val
        print preOrder_digui(t.left)
        print preOrder_digui(t.right)

preOrder_digui(troot)
