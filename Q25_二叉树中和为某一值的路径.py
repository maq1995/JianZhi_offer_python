# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/9 下午5:10
 @desc:
"""
'''
题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
     从树的根节点开始往下一直到叶节点所经过的结点形成一条路径。
     
解析：
    如下面的树：
            10
           /  \
          5    12
         / \
        4   7
    用上图的树为例：假如输入的整数是22，则打印出两条路径：10 5 7和 10 12
    在寻找路径的过程中，需要对树进行遍历，由于路径是从根节点出发到叶节点，也就是说路径总是以根节点为起始点，因此我们需要首先
遍历根节点，其中只有前序遍历（深度优先遍历）是先遍历根节点。那么按照前序遍历的顺序访问上面的树。
    首先访问根节点10，接下来访问结点5，因为需要打印路径，但是在本题中，二叉树的定义中没有父节点指针，所以访问的结点5的时候，我们
不知道前面经过了哪些结点，所以我们需要把经过的路径上的结点保存下来，每经过一个结点，我们把当前的结点添加到路径中去，到达结点5时，
路径中包含两个结点：10和5，接下来遍历结点4，此时路径中有三个结点10，5和4，此时路径的和为19，不等于22，所以要访问其他的路径，
从结点4回到结点5，并将路径中的结点4也删除，此时访问结点5的右子节点7，此时路径中有三个结点：10,5和7，此时路径的和为22，符合要求，
打印。然后回到结点10，访问10结点的右子节点12，此时到达叶节点，路径的和为22，符合，打印。
    可以看出保存路径元素的数据结构是一个栈。
    另外，可以在路径的形成过程中计算路径的和，也可以在路径完成之后再计算路径的和
'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_path(root, expectNumber):
    ret = []
    # 树为空
    if not root:
        return ret
    path = [root]
    sums = [root.data]

    def find_path_core(root):
        if root.left:
            path.append(root.left)
            sums.append(sums[-1]+root.left.data)
            find_path_core(root.left)
        if root.right:
            path.append(root.right)
            sums.append(sums[-1] + root.right.data)
            find_path_core(root.right)
        if not root.left and not root.right:
            if sums[-1] == expectNumber:
                ret.append([p.data for p in path])

        path.pop()
        sums.pop()

    find_path_core(root)
    return ret


node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(12)
node4 = TreeNode(4)
node5 = TreeNode(7)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

print find_path(node1, 19)





