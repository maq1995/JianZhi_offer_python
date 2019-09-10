# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/9 下午3:35
 @desc:
"""
'''
题目:从上到下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。

解析：
    这道题的实质是考察树的遍历算法，只不过这是层次遍历。层次遍历没有前序、中序、后序遍历的代码简单。
    如下面的这棵树：
                 8
                / \
               6   10
              / \   / \
              5  7  9  11
    我们开始分析层次遍历的过程：
    先打印根节点8，接下来我们需要打印8的两个子节点6和10，所以我们应该在遍历到8时将6和10保存到一个容器中，现在容器中有两个元素：
6和10，然后我们从容器中取出第一个元素6，将其子节点5和7放入到容器中，此时容器中有3个元素：10、5和7，接着取出10， 将10的子节点9
和11放入容器，此时容器中有4个元素：5、 7、 9、 11.   可以发现该数据结构为队列，先入先出。
'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def bfs(root):
    if not root:
        return None
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.data)
        if node.left_child is not None:
            queue.append(node.left_child)
        if node.right_child is not None:
            queue.append(node.right_child)
    return result


node1 = TreeNode(8)
node2 = TreeNode(6)
node3 = TreeNode(10)
node4 = TreeNode(5)
node5 = TreeNode(7)
node6 = TreeNode(9)
node7 = TreeNode(11)
node8 = TreeNode(2)
node9 = TreeNode(3)
node1.left_child = node2
node1.right_child = node3
node2.left_child = node4
node2.right_child = node5
node3.left_child = node6
node3.right_child = node7
node5.left_child = node8
node5.right_child = node9

print bfs(node1)



'''
题目：如何广度优先遍历一个有向图？

解析：
    树是图的一种特殊退化形式，不管是广度优先遍历一个有向图还是一棵树，都要用到队列。
    步骤：我们把起始节点（对树而言是根节点）放入队列中，接下来每一次从队列中的头部取出一个节点，遍历该节点之后能到达的节点（
    对树而言是其全部子节点）都依次放入队列，重复这个过程，直到队列中的节点全部被遍历为止。
'''

# 另外：Python中对图的定义 ： 邻接表  或者是 邻接矩阵
class Graph:
    def __init__(self, node_nums):
        self.adj =[[] for _ in range(node_nums)]  # 邻接表

    def add_edge(self, s, t):
        self.adj[s].append(t)
