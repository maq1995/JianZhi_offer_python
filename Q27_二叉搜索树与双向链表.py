# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/10 上午10:05
 @desc:
"""
'''
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
     要求不能创建任何新的结点，只能调整树中的结点指针的指向。
     
解析：
    在二叉树中，每个结点都有两个指向子节点的指针，在双向链表中，每个结点也有两个指针，分别指向前一个结点和后一个结点。
    由于要求转换之后的链表是有序的，我们可以用中序遍历树中的每一个结点。，因为中序遍历的特点就是按照从小到大的顺序遍历二叉搜索树。
    当遍历到根节点时，我们把树看成3部分：根节点，左子树和右子树。在把左右子树都转换成排序的双向链表之后再和根节点连接起来，整棵
二叉搜索树也就转换成了排序的双向链表。自然而然想到了递归。
'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convert(root):
    if not root:
        return None
    p_last = convert_nodes(root, None)

    while p_last and p_last.left:
        p_last = p_last.left
    return p_last


def convert_nodes(root, pLastNodeInList):
    if not root:
        return None
    if pLastNodeInList:
        s = pLastNodeInList.data
        l = pLastNodeInList.left is None
        r = pLastNodeInList.right is None
    if root.left:
        pLastNodeInList = convert_nodes(root.left, pLastNodeInList)
    if pLastNodeInList:
        pLastNodeInList.right = root
    root.left = pLastNodeInList
    pLastNodeInList = root

    if root.right:
        pLastNodeInList = convert_nodes(root.right, pLastNodeInList)

    return pLastNodeInList


# node1 = TreeNode(10)
# node2 = TreeNode(6)
# node3 = TreeNode(14)
# node4 = TreeNode(4)
# node5 = TreeNode(8)
# node6 = TreeNode(12)
# node7 = TreeNode(16)
# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5
# node3.left = node6
# node3.right = node7

# node1 = TreeNode(10)
# result = convert(node1)
# while result:
#     print result.data
#     result = result.right


"""
解法2：
"""


def Convert2(pRootOfTree):
    # write code here
    # 二叉搜索树的中序遍历是一个有序的序列，所以我们将采用中序遍历
    # 树里面的很多算法 都可以用递归实现
    if not pRootOfTree:
        return pRootOfTree
    if not pRootOfTree.left and not pRootOfTree.right:
        return pRootOfTree

    # 处理左子树
    Convert2(pRootOfTree.left)
    left = pRootOfTree.left
    # 连接根节点与左子树的最大值
    if left:
        while left.right:
            left = left.right
        pRootOfTree.left, left.right = left, pRootOfTree

    # 处理右子树
    Convert2(pRootOfTree.right)
    # 连接根节点与右子树的最小值
    right = pRootOfTree.right
    if right:
        while right.left:
            right = right.left
        pRootOfTree.right, right.left = right, pRootOfTree

    # 找到双向链表的头
    while pRootOfTree.left:
        pRootOfTree = pRootOfTree.left

    return pRootOfTree


# node1 = TreeNode(10)
# node2 = TreeNode(6)
# node3 = TreeNode(14)
# node4 = TreeNode(4)
# node5 = TreeNode(8)
# node6 = TreeNode(12)
# node7 = TreeNode(16)
# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5
# node3.left = node6
# node3.right = node7

# node1 = TreeNode(10)
# result = convert(node1)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node3.left = node2
node3.right = node4
node2.left = node1
node4.right = node5

result = Convert2(node3)
while result:
    print result.data
    result = result.right