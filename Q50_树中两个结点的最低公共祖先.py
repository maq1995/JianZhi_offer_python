# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/18 下午5:06
 @desc:
"""
'''
题目：输入树的两个结点，求它们的最低公共祖先。
'''

'''
解析1：
    先假设该树是二叉搜索树。
    那么因为二叉搜索树是排序的，位于左子树的结点都比父节点小，位于右子树的结点都比父节点大。我们只需要从树的根节点开始和两个输入
的结点进行比较，如果当前结点的值比两个结点都大，那么其最低公共祖先一定在当前结点的左子树中，如果当前结点的值比两个结点都小，说明
其最低公共祖先一定在当前结点的右子树中。这样在树中从上到下找到的第一个在两个输入结点的值之间的结点，就是最低的公共祖先。
'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def searchTree_find_lowest_parent(root, node1, node2):
    if not root or not node1 or not node2:
        return None
    while root:
        if root.data > node1.data and root.data > node2.data:
            root = root.left_child
        elif root.data < node1.data and root.data < node2.data:
            root = root.right_child
        else:
            return root

    return None


# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)
# node6 = TreeNode(6)
# node7 = TreeNode(7)
# node8 = TreeNode(8)
# node9 = TreeNode(9)
# node10 = TreeNode(10)
#
# node5.left_child = node3
# node5.right_child = node8
# node3.left_child = node2
# node3.right_child = node4
# node2.left_child = node1
# node8.left_child = node7
# node8.right_child = node9
# node7.left_child = node6
# node9.left_child = node10

# n = searchTree_find_lowest_parent(node5, node10, node7)
# if n:
#     print n.data
# else:
#     print "not find the lowest parent"

'''
解析2：
    该树不是二叉搜索树，仅仅是普通的一棵树，甚至都不是二叉树。
    但是每个结点有指向父节点的指针。
    该题可以转换为求两条链表的第一个公共结点。
    思路1：分别把两个链表的结点放入到两个栈中，这样两个链表的尾结点就位于两个栈的栈顶，接下来比较两个栈顶的结点是否相同，如果相
          同则把栈顶元素弹出接着比较下一个栈顶，直到找到最后一个相同的结点。
          
    思路2：我们可以先遍历两个链表得到它们的长度，得到长的链表比短的链表多几个结点，在第二次遍历的时候，在长链表上先走若干步，然后
          再开始同步遍历，找第一个相同的结点
    
    这里采用思路1
'''


class TreeNode2:
    def __init__(self, data):
        self.data = data
        self.first_child = None
        self.second_child = None
        self.third_child = None
        self.parent = None


def hasParentPoint_find_lowest_parent(node1, node2):
    if not node1 or not node2:
        return None

    stack1 = []
    while node1:
        stack1.append(node1)
        node1 = node1.parent

    stack2 = []
    while node2:
        stack2.append(node2)
        node2 = node2.parent

    lowest_parent = None
    i = len(stack1) - 1
    j = len(stack2) - 1
    while j >= 0 and i >= 0:
        a = stack1[i].data
        b = stack2[j].data
        if stack2[j].data == stack1[i].data:
            lowest_parent = stack1[i]
            i -= 1
            j -= 1

        else:
            break
    c = lowest_parent.data
    return lowest_parent


# node5 = TreeNode2(5)
# node10 = TreeNode2(10)
# node4 = TreeNode2(4)
# node2 = TreeNode2(2)
# node9 = TreeNode2(9)
# node99 = TreeNode2(99)
# node13 = TreeNode2(13)
# node22 = TreeNode2(22)
# node18 = TreeNode2(18)
#
# node5.first_child = node10
# node5.second_child = node4
# node5.third_child = node2
# node10.parent = node5
# node4.parent = node5
# node2.parent = node5
# node10.first_child = node9
# node10.third_child = node99
# node9.parent = node10
# node99.parent = node10
# node4.first_child = node13
# node13.parent = node4
# node2.first_child = node22
# node2.second_child = node18
# node22.parent = node2
# node18.parent = node2
#
# n = hasParentPoint_find_lowest_parent(node9, node10)
# if n:
#     print n.data
# else:
#     print "not find lowest parent"


'''
解析3：
    树是普通的树，不是二叉树，也没有指向父节点的指针。
    先求出两个结点到根结点的路径，然后从路径中找出最后一个公共结点。
'''


def get_path(root, node, ret):
    if not root or not node:
        return False
    ret.append(root)
    if root == node:
        return True
    left = get_path(root.left_child, node, ret)
    right = get_path(root.right_child, node, ret)
    if left or right:
        return True
    ret.pop()


def get_last_commen_node(root, node1, node2):
    route1 = []
    route2 = []
    ret1 = get_path(root, node1, route1)
    ret2 = get_path(root, node2, route2)
    ret = None
    if ret1 and ret2:
        lenght = len(route1) if len(route1) <= len(route2) else len(route2)
        index = 0
        while index < lenght:
            if route1[index] == route2[index]:
                ret = route1[index]
            index += 1

    return ret


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)

node5.left_child = node3
node5.right_child = node8
node3.left_child = node2
node3.right_child = node4
node2.left_child = node1
node8.left_child = node7
node8.right_child = node9
node7.left_child = node6
node9.left_child = node10

n = get_last_commen_node(node5, node1, node4)
if n:
    print n.data
else:
    print "not found lowest parent"
