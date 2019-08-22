# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/22 下午3:17
 @desc:
"""
'''
题目：输入两颗二叉树A和B，判断B是不是A的子结构

解析：
    要查找树A中是否存在和树B结构一样的子树，饿哦们可以分为两步：第一步在树A中找到和B的根节点的值一样的结点R，第二步再判断
    树A中以R为根节点你的子树是不是包含和树B一样的结构。

代码鲁棒性：
'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def HasSubTree(root1, root2):
    result = False

    if root1 and root2:
        if root1.data == root2.data:
            result = DoseTree1HaveTree2(root1, root2)
        if result is False:
            result = HasSubTree(root1.left, root2)
        if result is False:
            result = HasSubTree(root1.right, root2)

    return result


def DoseTree1HaveTree2(root1, root2):
    if root2 is None:
        return True
    if root1 is None:
        return False

    if root1.data != root2.data:
        return False

    return DoseTree1HaveTree2(root1.left, root2.left)  and DoseTree1HaveTree2(root1.right, root2.right)


pRoot1 = TreeNode(8)
node1 = TreeNode(8)
node2 = TreeNode(7)
node3 = TreeNode(9)
node4 = TreeNode(2)
node5 = TreeNode(4)
node6 = TreeNode(7)
pRoot1.left = node1
pRoot1.right = node2
node1.left = node3
node1.right = node4
node4.left = node5
node4.right = node6

pRoot2 = TreeNode(8)
node7 = TreeNode(9)
node8 = TreeNode(2)
pRoot2.left = node7
pRoot2.right = node8

print HasSubTree(pRoot1, None)