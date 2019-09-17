# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/16 下午3:58
 @desc:
"""
'''
题目：输入一棵二叉树的根节点，求该树的深度，从根节点到叶节点依次经过的结点（含根、叶节点）形成数的一条路径，最长路径的长度为树的深度。

解析：
    在题目25中，我们讨论了如何记录树中的路径，但是这种思路的代码量较大，本题使用更加简介的方法。
    我们从另一个角度来理解树的深度。如果一棵树只有一个结点，那么它的深度为1；如果根节点只有左子树没有右子树，那么树的深度为左子树的
深度加1；如果根节点既有左子树又有右子树，那么该树的深度为其左、右子树深度的较大值加1.
    这个思路使用递归的方式很容易实现，只需要对遍历的代码稍作修改即可。
'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


def TreeDepth(root):
    if root is None:
        return 0
    # if not root.lchild and root.rchild:
    #     return 1

    left = TreeDepth(root.lchild)
    right = TreeDepth(root.rchild)
    return max(left, right) + 1


# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)
# node6 = TreeNode(6)
# node7 = TreeNode(7)
# node8 = TreeNode(8)
#
# node1.lchild = node2
# node1.rchild = node3
# node2.lchild = node4
# node2.rchild = node5
# node3.rchild = node6
# node5.lchild = node7
# node7.lchild = node8

# print TreeDepth(node1)


'''
题目2：输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意结点的左右子树的深度相差不超过1，那么它是一棵平衡二叉树。
'''

'''
解法1：有了上面求解二叉树的深度的经验之后，我们可以很容易的想到一个思路：在遍历树的每个结点时，调用函数TreeDepth得到它左右子树的深度，
      如果每个结点的左右子树的深度相差都不超过1，按照定义，它就是一棵平衡二叉树
'''


def isBalanceTree(root):
    if root is None:
        return True
    left = TreeDepth(root.lchild)
    right = TreeDepth(root.rchild)
    diff = left - right
    if diff > 1 or diff < -1:
        return False

    return isBalanceTree(root.lchild) and isBalanceTree(root.rchild)


'''
解法2：解法1虽然简洁，但是我们注意到一个结点会被重复遍历多次。
     下面来介绍一种不需要重复遍历的方法。
     如果我们用后序遍历的方法遍历二叉树的每一个结点，在遍历到一个结点之前，我们已经遍历了它的左右子树，只要在遍历每个结点的时候
记录它的深度，我们就可以一边遍历一边判断每个结点是不是平衡的。
'''
# 未实现


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node1.lchild = node2
node1.rchild = node3
node2.lchild = node4
node2.rchild = node5
# node5.lchild = node6

print isBalanceTree(node1)
