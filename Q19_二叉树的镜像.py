# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/23 下午2:22
 @desc:
"""
'''
题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像

解析：
    自己画出一棵树和其镜像树，观察之后可以发现求一棵树的镜像的过程：我们前序遍历这棵树的每个结点，如果遍历到的结点有子节点，
    就交换它的两个子节点，当交换完所有非叶子节点的左右子节点之后,就得到了树的镜像。
'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 递归版本
def MirrorTreeRecuesively(root):
    if root is None or (root.left is None and root.right is None):
        return root
    else:
        leftChild = root.left
        rightChild = root.right
        root.left = rightChild
        root.right = leftChild

        if root.left is not None:
            MirrorTreeRecuesively(root.left)
        if root.right is not None:
            MirrorTreeRecuesively(root.right)


# root = TreeNode(8)
# node1 = TreeNode(6)
# node2 = TreeNode(10)
# node3 = TreeNode(5)
# node4 = TreeNode(7)
# node5 = TreeNode(9)
# node6 = TreeNode(11)
#
# root.left = node1
# root.right = node2
# node1.left = node3
# node1.right = node4
# node2.left = node5
# node2.right = node6
#
# # 前序遍历
# def preOrder(root):
#     if root:
#         print root.data
#         preOrder(root.left)
#         preOrder(root.right)
#
# preOrder(root)
#
# MirrorTreeRecuesively(root)
#
# print "---------------"
# preOrder(root)


# 循环版本
def MirrorTreeLoop(root):
    if root is None or (root.left is None and root.right is None):
        return root

    queue = [root]
    while queue:
        node = queue.pop(0)
        if node and (node.left is not None or node.right is not None):
            leftChild = node.left
            rightChild = node.right
            queue.append(leftChild)
            queue.append(rightChild)
            node.left = rightChild
            node.right = leftChild

    return root


root = TreeNode(8)
node1 = TreeNode(6)
node2 = TreeNode(10)
node3 = TreeNode(5)
node4 = TreeNode(7)
node5 = TreeNode(9)
node6 = TreeNode(11)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6


# 前序遍历
def preOrder(root):
    if root:
        print root.data
        preOrder(root.left)
        preOrder(root.right)


preOrder(root)

r = MirrorTreeLoop(root)
print "------------"
preOrder(r)
