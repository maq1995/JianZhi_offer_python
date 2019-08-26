# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/12 上午9:20
 @desc:
"""
'''
1.树的操作会涉及到大量的指针
2.二叉树是树的一种特殊结构，在二叉树中最重要的操作莫过于遍历，即按照某一顺序访问树中的所有结点。
通常数有以下几种遍历方式：
    A.前序遍历： 先访问根节点，再访问左子节点，最后访问右子节点
    B.中序遍历： 先访问左子节点，再访问根节点，最后访问右子节点
    C.后序遍历： 先访问左子节点，再访问右子节点，最后访问根节点
        这三种遍历都有递归和循环两种实现方法(需要熟练掌握)。
    D.宽度/广度优先遍历： 先访问树的第一层结点，再访问树的第二层结点......，直到最后一层结点
    E.深度优先遍历： 只要当前结点存在子结点，就先访问其子节点，再访问当前结点
3.非空二叉树的第n层上至多有2^(n-1)个元素， 深度为h的二叉树至多有2^h - 1个结点
4.完全二叉树：除了最大的层次即成为一个满二叉树亲切层次最大那层所有点结点均向左靠齐，即集中在左边的位置上，不能有空位置。
  对于完全二叉树，设一个结点为i,则其父节点为i/2，左子节点为2i，右子节点为2i+1
5.二叉树通常使用链式存储
'''


"""
#### 前序遍历 递归版本
def preOrder_digui(t):
    if t is not None:
        print t.data
        preOrder_digui(t.left)
        preOrder_digui(t.right)
        
#### 前序遍历 循环版本（非递归）
# 对于任意结点node，首先访问之（输出其值），然后判断其左子树是否为空，不空时，重复上面的步骤，直到其为空，
                                                            若为空，则需要访问右子树。
# 注意：在访问过左孩子之后，需要返回来访问其右孩子，所以需要用到栈这种数据结构
# 具体： 对于任意的结点node,
# a) 访问之，并将node结点入栈，当前结点置为左孩子
# b) 判断当前结点node时候为空，若为空，则取出栈顶结点并出栈，将右孩子置为当前结点；
                            否则，重复步骤a)直到当前结点为空或者栈为空。
def preOrder_xunhuan(t):
    stack = []
    while t is not None or s.Empty() is False:
        if t is not None:
            print t.data
            stack.push(t)
            t = t.left
        else:
            node = s.pop()
            t = node.right


#### 中序遍历 递归版本
def inOrder_digui(root):
    if root is not None:
        inOrder_digui(root.left)
        print root.data
        inOrder_digui(root.right)
        
### 中序遍历 循环版本
def inOrder_xunhuan(root):
    stack = []
    while root is not None or s.isEmpty is False:
        if root is not None:
            stack.push(root)
            root = root.left
        else:
            node = stack.pop()
            print node.data
            root = node.right
            
#### 后序遍历  递归版本
def postOrder_digui(root):
    if root is not None:
        postOrder_digui(root.left)
        postOrder_digui(root.right)
        print root.data   


#### 后序遍历 循环版本
# 后序遍历的循环版本比较麻烦
def postOrder_xunhuan(root):
    stack1 = []
    stack2 = []
    stack1.push(root)
    while stack1.isEmpty is Fasle:
        tempNode = stack1.pop()
        if tempNode.left != None:
            stack1.push(tempNode.left)
        if tempNode.right != None:
            stack1.push(tempNode.right)
        stack2.push(tempNode)
    
    while stack2.isEmpty is Fasle:
        print stack2.pop().data 
        
        
#### 广度优先遍历
# 也叫作层次遍历  可以使用队列实现
def levelTranverse(root):
    queue = [] 
    queue.push(root)
    while queue.isEmpty is False:
        none = queue.pop(0)  # 弹出队首元素
        print node.data
        if node.left is not None:
            queue.push(node.left)
        if node.right is not None:
            queue.push(node.right)
            
#### 深度优先遍历和前序遍历一样。            
    
            
"""


"""
特殊的二叉树之一：
    1.二叉搜索树： 在二叉搜索树中，左子节点总是小于或等于根节点，右子节点总是大于或等于根节点。我们可以平均在O（logn）的时间内
根据数值在二叉搜索树中找到一个结点。（n是节点数）

这里使用Python来实现一个二叉搜索树
树结点的定义：
class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

树的定义：
class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)
    
    # 搜索
    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)
            
    # 插入
    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node 
    # 删除
    # 如果待删除结点是叶子结点，则可以被直接删除
    # 如果该待删除结点只有一个子节点，则将此结点的父节点指向该结点的子节点即可，然后删除该结点
    #　如果该待删除结点有两个儿子，则将其右子树的最小数据代替此结点的数据，并将其右子树的最小数据删除
    def delete(self, root, data):
        flag, n, p = self.search(root, root, data)
        if flag is False:
            print "this data is not in the tree"
        
        else:
            # 待删除结点是叶子结点
            if n.lchild is None and n.rchild is None:
                if n == p.lchild:
                    p.lchild = None
                else:
                    p.rchile = None
                del n
                return 
                
            # 待删除结点只有一个子节点
            elif n.lchild is None:
                if n == p.lchile:
                    p.lchild = n.rchild
                else:
                    p.rchild = n.rchild
                del n
                return
            elif n.rchild is None:
                if n == p.lchile:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
                del n
                return 
                
            # 待删除结点有两个子节点, 则将其右子树的最小数据代替此结点的数据，并将其右子树的最小数据删除
            else:
                pre = n.rchild
                if pre .lchild == None:
                    n.data = pre.data
                    n.rchild = pre.rchild
                    del pre
                    return
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del next
                    return
    
    # 前序遍历
    # 中序遍历
    # 后序遍历
    def ...




if __name__ == '__main__':
a  = [49, , 65, 97, 60, 76, 13, 27, 5, 1]
bst = BST(a)
bst.前序遍历（）
...
"""


"""
特殊的二叉树之二：
    2.堆：堆也被称为优先队列。队列中允许的操作是先进先出，在队尾插入元素，在队头取出元素，而堆也一样，在堆底插入元素，在堆顶取出
元素。但是堆中元素的排列不是按照到达的先后顺序，而是按照一定的优先循序排列的，这个优先顺序可以是元素的大小或者其他规则。堆一般分为
最大堆和最小堆。最大堆中根节点的值最大，并且每一个分支都可以看成一个最大堆。最小堆的定义与之对应。

最大堆的插入：先插入到最后一个元素的后面（完全二叉树的形式），然后将该元素持续与其父节点对比，如果大于父节点，则交换，直到小于父节点或者到达根节点。
最大堆的删除：删除的是堆顶，然后将最后一个元素放到根节点中，然后比较该结点与其两个子节点的大小，将最大值放在父节点上。
最小堆的插入和删除类似。

Python中，堆可以使用数组、列表实现：一个下标为j的结点的父节点为int((j-1)/2)
也可以使用二叉树的结构来实现堆。
另外Python中有内置的堆实现：heapq
使用：
    import heapq as hq
    data = np.arange(10)
    data = np.randomshuffle(data)
    heap = []
    for i in data:
        hq.heappush(heap, i)
    hq.heappop(heap)

"""


"""
特殊的二叉树之三：
    3.红黑树：二叉搜索树最好情况是O（logn）,但是如果插入元素是有序的，则生成的二叉排序树就是一个链表，这种情况下，需要遍历全部
元素才行，O（n）。
A.红黑树介绍
    红黑树是针对这一情形进行改进。红黑树本质上是一种二叉搜索树，但它在二叉搜索树的基础上额外添加了一个标记（颜色），同时具有一定的
规则，这些规则使得红黑树保证一种平衡，插入、删除、查找的最坏时间复杂度都为O（logn）。【红黑树的统计性能要好于平衡二叉树。】
红黑树的在原有的二叉搜索树上增加了如下几个要求：
    1）每个结点要么是红色，要么是黑色
    2）根节点永远是黑色的
    3）所有叶子结点都是黑色的（红黑树中的叶子结点都是空结点。）
    4）每个红色结点的两个子结点一定都是黑色的（说明从根到结点的路径上不会有两个连续的红色结点，但黑色结点可以是连续的）
    5）从任一结点到其子树中每个叶子结点的路径都包含相同数量的黑色结点。（是成为红黑树最主要的条件，后序的插入、删除操作都是为了遵守这个规定）
    
    红黑树并不是标准的平衡二叉树，它是以上述要求作为一种平衡方法，使一棵n个结点的红黑树始终保持了logn的高度，使得自己的性能得到提升。
    
B.红黑树的旋转
    当对红黑树进行插入和删除等操作时，对树做了修改可能会破坏红黑树的性质。为了继续保持红黑树的性质，可以通过对结点进行重新着色，
以及对树进行相关的旋转操作，即通过修改树中某些结点的颜色及指针结构，来达到对红黑树进行插入或删除结点等操作后继续保持它的性质或平衡的目的。
    1）左旋操作：当在某个结点pivot上，做左旋操作时，我们假设它的右孩子不是NIL（叶子结点），pivot可以为任何不是NIL的左子节点。
左旋以pivot到其右孩子之间的链为“支轴”进行，使得其右孩子成为该子树的新根，而右孩子的左孩子成为pivot的右孩子。
    2）右旋操作：与左旋操作类似，当在某个结点pivot上做右旋操作时，以pivot和其左孩子之间的链为轴，使得其左孩子成为该子树的新根，
而左孩子的右孩子作为pivot的左孩子。

## 左旋伪代码
def leftRoate(T, x):
    y = x.right
    x.right = y.left  #  y的左孩子成为x的右孩子
    if y.left != NIL
        y.left.parent = x  #  x的父结点成为y的父结点
    y.parent = x.parent
    if x.parent = NIL:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y 
    else:
        x.parent.left = y
    y.left = x
    x.parent = y
    
### 右旋代码
# 右旋操作：与左旋操作类似，当在某个结点pivot上做右旋操作时，以pivot和其左孩子之间的链为轴，使得其左孩子成为该子树的新根，
# 而左孩子的右孩子作为pivot的左孩子。
def rightRoate(T, x):
    y = x.left
    x.left = y.right  #  y的左孩子成为x的右孩子
    if y.right != NIL
        y.right.parent = x  #  x的父结点成为y的父结点
    y.parent = x.parent
    if x.parent = NIL:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y 
    else:
        x.parent.left = y
    y.right = x
    x.parent = y

    树在经过左旋右旋之后，树的搜索性质保持不变，但树的红黑性质则被破坏了，所以，红黑树插入和删除数据后，需要利用旋转与颜色重涂来
重新恢复树的红黑性质。

C.红黑树的插入
首先来了解一下二叉搜索树的插入：
伪代码：
def Tree-Insert(T, z):  # T是一棵树，z是要插入的结点
    y = NIL
    x = T.root
    while x != NIL:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == NIL:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
红黑树的插入所示在二叉搜索树的基础上，为了重新回复平衡，继续做了插入修复操作。
红黑树插入的伪代码如下：假设插入的结点为z，
RB-INSERT(T, z)
y = NIL
x = T.root
while x != NIL:
    y = x
    if z.key < x.key:
        x = x.left
    x = x.right
    
z.parent = y
if y == NIL:
    T.root = z
elif z.key < y.key:
    y.left = z
else:
    y.right = z
z.left = NIL
z.right = NIL
z.color = red  #  新插入的结点先设置为红色
RB-INSERT-FIXUP(T, z)  # 调整红黑树


# 如果插入的结点如果是根节点，即原树是空树，此情况只会违反性质2），因此直接将该结点涂为黑色
# 如果插入的结点的父节点是黑色，则不会违反要求2）和4），此时什么都不用做
# 上面两种情况很简单，下面的情况比较复杂
# case1:如果插入的结点的父节点是红色，且叔叔结点也是红色
    此时插入结点一定存在祖父结点，该情况又分为其父节点是祖父结点的左孩子还是右孩子
    当其父节点是左孩子时：将当前结点的父节点和叔叔结点涂黑，祖父结点涂红，把当前结点指向祖父结点，从新的当前结点重新开始算法
    当其父节点是右孩子时，与左孩子是算法相同
# case2:如果插入的结点的父节点是红色，且叔叔结点是黑色，当前结点是其父节点的右孩子
    当前结点的父节点最为新的当前结点，以新的当前结点为支点进行左旋操作
# case3:如果插入的结点的父节点是红色，且叔叔结点是黑色，当前结点是其父节点的左孩子
    将当前结点的父节点变为黑色，祖父结点变为红色，以祖父结点为支点进行右旋操作
RB-INSERT-FIXUP(T, z)
while z.parent.color == RED:
    if z.parent = z.parent.parent.left: # 其父节点是祖父结点的左孩子
        y = z.parent.parent.right  # y 是其叔叔结点
        if y.color == RED:          # case 1 父节点为红色，叔叔结点也为红色
            # 父节点是红色，且叔叔结点也是红色
            # 当父节点是左孩子时：将当前结点的父节点和叔叔结点涂黑，祖父结点涂红，把当前结点指向祖父结点，从新的当前结点重新开始算法
            z.parent.color = BLACK
            y.color = BLACK
            z.parent.parent.color = RED
            z = z.parent.parent
        elif z == z.parent.right:  # case 2 叔叔结点为黑色， 且当前结点是其父节点的右孩子
            # 当前结点的父节点最为新的当前结点，以新的当前结点为支点进行左旋操作
            z = z.parent
            LEFT-ROTATE(T, z)
        elif z == z.parent.left:  # case 3 叔叔结点为黑色，且当前结点是其父节点的左孩子
            # 将当前结点的父节点变为黑色，祖父结点变为红色，以祖父结点为支点进行右旋操作
            z.parent.color = BLACK  
            a.parent.parent.color = RED
            RIGHT-ROTATE(T, z.p.p)

    else:  # # 其父节点是祖父结点的右孩子
         y = z.parent.parent.right  # y 是其叔叔结点
         if y.color == RED:          # case 1 父节点为红色，叔叔结点也为红色
            # 父节点是红色，且叔叔结点也是红色
            # 当父节点是右孩子时：将当前结点的父节点和叔叔结点涂黑，祖父结点涂红，把当前结点指向祖父结点，从新的当前结点重新开始算法
            z.parent.color = BLACK
            y.color = BLACK
            z.parent.parent.color = RED
            z = z.parent.parent
         elif  z == z.parent.right:  # case 2 叔叔结点为黑色， 且当前结点是其父节点的右孩子
            # 将当前结点的父节点变为黑色，祖父结点变为红色，以祖父结点为支点进行左旋操作
            z.parent.color = BLACK
            z.parent.parent.color = RED
            LEFT-ROTATE(T, z.parent.parent)
         elif z == z.parent.left:  # case 3 叔叔结点为黑色，且当前结点是其父节点的左孩子
            # 当前结点的父节点最为新的当前结点，以新的当前结点为支点进行右旋操作
            z = z.parent
            RIGHT-ROTATE(T, z)
    
T.root.color = BLACK  # 将根节点涂为黑色

####  红黑树插入总结：
1.插入结点设置为红色
2.如果插入结点为根节点，则将其置为黑色，return
3.如果插入结点的父节点为黑色，什么都不用做，return
4.如果插入结点的父节点为红色：
    1）父节点是祖父节点的左孩子：
        A. 叔叔结点为红色： 
            将当前结点的父节点和叔叔结点涂黑，祖父结点涂红，把当前结点指向祖父结点，从新的当前结点（即祖父结点）重新开始算法
        B. 叔叔结点为黑色， 插入结点为父节点的右孩子：
            当前结点的父节点最为新的当前结点，以新的当前结点为支点进行左旋操作
        C. 叔叔结点为黑色， 插入结点为父节点的左孩子：
            当前结点的父节点变为黑色，祖父结点变为红色，以祖父结点为支点进行右旋操作
    2）父节点是祖父结点的右孩子：
         A. 叔叔结点为红色： 
            将当前结点的父节点和叔叔结点涂黑，祖父结点涂红，把当前结点指向祖父结点，从新的当前结点（即祖父结点）重新开始算法
        B. 叔叔结点为黑色， 插入结点为父节点的右孩子：
            将当前结点的父节点变为黑色，祖父结点变为红色，以祖父结点为支点进行左旋操作
        C. 叔叔结点为黑色， 插入结点为父节点的左孩子：
            当前结点的父节点最为新的当前结点，以新的当前结点为支点进行右旋操作


D.红黑树的删除
先了解以下二叉搜索树结点删除的几种情况
1.删除结点为叶节点：直接将父节点对应的儿子指针设为NULL，删除儿子结点即可
2.删除的结点b有一个儿子c，那么将删除结点的父节点a的相应儿子指针指向c，删除b即可
3.删除的结点有两个儿子：将其左子树的最大元素值代替该值，删除最大元素的结点即可

红黑树的删除情况比较复杂：
####
case 1.被删除结点无子节点，且被删除结点为红色:
    策略： 直接将该结点删除即可，不会破幻红黑树的性质

#### 
case 2.被删除结点无子节点，且被删除结点为黑色
    删除黑色结点会破幻红黑树的性质5），所以为了不破坏性质5），在替换节点上增加一个一重黑色。这里额外一重黑色是什么意思呢，我们
不是把红黑树的节点加上除红与黑的另一种颜色，这里只是一种假设，我们认为我们当前指向它，因此空有额外一种黑色，可以认为它的黑色是从
它的父节点被删除后继承给它的，它现在可以容纳两种颜色，如果它原来是红色，那么现在是红+黑，如果原来是黑色，那么它现在的颜色是黑+黑。
有了这重额外的黑色，原红黑树性质5就能保持不变。
    #####
    A. 被删除结点node的brother结点为黑色，且brother结点有一个与其自身方向一致的红色子节点son (son称为node的远侄子结点)
策略：当node为左孩子：
        将父节点father和兄弟节点brother的颜色对调，然后以父节点father为支点，进行左旋操作，再将之前的红色son结点变为黑色即可。
     当node为右孩子：
        将父节点father和兄弟节点brother的颜色对调，然后以父节点father为支点，进行右旋操作，再将之前的红色son结点变为黑色即可。
     

图解： node为左孩子
    (下图中--b 表示黑色，  --r 表示红色，  --+黑色 表示替换结点加一重黑色， 及诶单后面没有加--b/r的表示什么颜色都可以)
        father                                       brother                              
         /  \                                       /      \   
    node--b  brother--b    删除node后调整      father-b    son--b(原来为红色，调整之后涂为黑色)
              /  \                                \         / \
        leftson   son--r                         leftson   a   b
                  /  \ 
                  a   b                                     
图解： node为右孩子时：
                 father                                      brother                  
                 /     \                                      /     \
         brother--b    node--b        删除node后调整        son--b  father --b
           /      \                                         / \        /
        son--r  rightson                                    a  b   rightson
         /  \ 
         a   b                                     

    #####
    B. 被删除结点node的brother结点为黑色，且brother结点有一个与其自身方向不一致的红色子节点son(son称为node的近侄子结点)
策略：当node为左孩子：
         以近侄子节点为支点，进行右旋，并将近侄子节点的颜色与兄弟结点节点的颜色进行互换, 此时情况变为case2.A
     当node为右孩子：
         将近侄子节点的颜色和兄弟结点的颜色互换，并以近侄子节点为支点，进行左旋操作, 此时情况变为case2.A
图解： node为左孩子
        father                                     father
        /    \                                     /    \
    node--b  brother--b         调整           node--b   son--b
             /      \                                    / \
           son--r   rightson                               brother--r
                                                             /   \
                                                                rightson
图解： node为右孩子
              father                                     father
              /      \                                   /     \
        brother--b    node--b     调整               son--b    node--b
         /       \                                  /    \  
    leftson    son--r                       brother--r    
                                                /
                                            leftson

    
    #####
    C. 被删除结点node的brother结点为黑色，且brother结点没有红色子结点
    此时又可以分为两种情况：father结点为红色、father结点为黑色
        1）当father结点为红色时，因为被删除结点node没有子节点，根据红黑树的性质可知，brother结点也一定没有子节点
        策略： 将father的颜色和brother的颜色互换，然后删除node即可。
        2）当father结点为黑色时，因为被删除结点node没有子节点，根据红黑树的性质可知，brother结点也一定没有子节点
        策略： 将brother的颜色改为红色，这样删除node之后，father左右两支的黑色节点数就相等了，但是经过father结点的路径上的
              黑色节点数会减少1，这个时候，我们再以father为起始点，继续根据情况进行平衡操作（将father结点当做node结点，只是
              不再进行删除操作。），观察是什么情况，再进行相应的调整，这样一直向上，直到新的起始点为根节点
    
    #####
    D. 被删除结点node的brother结点为红色， 则其父节点一定为黑色
        策略：当被删除结点为左结点时，将父节点和兄弟结点的颜色互换，然后以父节点为支点，进行左旋操作
             当被删除结点为右结点时，将父节点和兄弟结点的颜色互换，然后以父节点为支点，进行右旋操作
    
    
    总结：判断类型的时候，先看待删除的节点的颜色，再看兄弟节点的颜色，再看侄子节点的颜色（侄子节点先看远侄子再看近侄子），
         最后看父亲节点的颜色

####    
case 3.被删除结点只有一个子节点，且被删除结点为红色  --- 该情况不存在
    这种情况是不存在的，会破坏红黑树的性质5）
       node--red
        /       \
value--black    NIL-black
     /  \
    NIL NIL

####    
case 4.被删除结点只有一个子节点，且被删除结点为黑色
    策略： 在这种情况下，被删除结点的非NIL子节点肯定为红色， 删除node之后，将其子节点代替该结点，并涂黑即可
         node--black                                value--black
        /       \                                      /   \           
  value--red   NIL-black         删除node之后         NIL    NIL    
     /  \
    NIL NIL

####   
case 5&6.被删除结点有两个子节点，且被删除结点为黑色或红色
    当被删除结点node有两个子节点时，先要找到倍删除结点的后继结点successor(此处successor为右子树中的最小值)，
      node                    node
      /  \                     /  \
    left  right              left  right----successor
   /      /    \                      \
      successor
    
    当successor在左边图的情况中时，使用successor代替node之后，相当于successor被删除，如果successor为红色，则变成了case1.
若successor为黑色，则变成了组合2
    当successor在右边图的情况中时，使用successor代替node之后，相当于successor被删除，如果successor为红色，则变成了case3，
不可能存在，所以successor只能为黑色，则变成了组合2或4.
    综上，若被删除及诶单是组合1或组合4的情况则很容易处理，如果是组合5&6的情况则将变为组合1或组合2或组合4
        
       
4.平衡二叉树（AVL树）， 也叫平衡二叉搜索树。
A.介绍
    定义：父节点的左子树和右子树的高度之差不能大于1，也就是说不能高过1层。否则该树就失衡了，此时就要旋转节点。
    它具有如下几个性质：
    1）.可以是空树。
    2）.假如不是空树，任何一个结点的左子树与右子树都是平衡二叉树，并且高度之差的绝对值不超过1
    
    在编码时，我们可以记录当前节点的高度，比如空节点是-1，叶子节点是0，非叶子节点的height往根节点递增，比如在下图
    中我们认为树的高度为h=2。
    
                       P  ----hight = 2
                      / \
       hight = 0--   Q   M   ----hight = 1
                         \
                            N  ---higth = 0

B.旋转
   平衡因子：左子树的高度减去右子树的高度，由平衡二叉树的定义可知，平衡因子的取值只可能为0,1,-1
   则平衡因子 P：1，  Q：0，  M：1， N：0
   
①插入新节点，调整：
   在新插入的结点向上查找，以第一个平衡因子的绝对值超过1的结点为根的子树称为最小不平衡子树。此时，我们只要
调整最小的不平衡子树，就能够将不平衡的树调整为平衡的树。
    `LL型：以失衡点为支点做右旋操作
    `RR型：以失衡点为支点做左旋操作
    `LR型： 先以拐点处为支点做左旋操作，再以失衡点为支点做右旋操作
    `RL型： 先以拐点处为支点做右旋操作，再以失衡点为支点做左旋操作
②：删除结点，调整
    （1）删除叶子节点,直接删除，当前节点（为None）的平衡不受影响
    （2）删除的节点只有左子树/右子树,用左儿子或右儿子代替当前节点，当前节点的平衡不受影响。
    （3）删除的节点既有左子树又有右子树,如果右子树高度较高，则从右子树选取最小节点，将其值赋予当前节点，然后删除右子树的
最小节点。如果左子树高度较高，则从左子树选取最大节点，将其值赋予当前节点，然后删除左子树的最大节点。这样操作当前节点的平衡
不会被破坏。
    


5.B树， B+树
B树是多叉树有名平衡多路查找树，又名B-树
（1）平衡二叉树节点最多有两个子树，而 B 树每个节点可以有多个子树，M 阶 B 树表示该树每个节点最多有 M 个子树
（2）平衡二叉树每个节点只有一个数据和两个指向孩子的指针，而 B 树每个中间节点有 k-1 个关键字（可以理解为数据）和 k 
个子树（ **k 介于阶数 M 和 M/2 之间，M/2 向上取整）
（3）B 树的所有叶子节点都在同一层，并且叶子节点只有关键字，指向孩子的指针为 null
（4）和平衡二叉树相同的点在于：B 树的节点数据大小也是按照左小右大，子树与节点的大小比较决定了子树指针所处位置。

B 树的定义，一棵 B 树必须满足以下条件：
（1）若根结点不是终端结点，则至少有2棵子树
（2）除根节点以外的所有非叶结点至少有 M/2 棵子树，至多有 M 个子树（关键字数为子树减一）
（3）所有的叶子结点都位于同一层
B 树的每个节点可以表示的信息更多，因此整个树更加“矮胖”，这在从磁盘中查找数据（先读取到内存、后查找）的过程中，可以
减少磁盘 IO 的次数，从而提升查找速度

平衡二叉树的平衡条件是：左右子树的高度差不大于 1；而 B 树的平衡条件则有三点：
（1）叶子节点都在同一层
（2）每个节点的关键字数为子树个数减一（子树个数 k 介于树的阶 M 和它的二分之一）
（3）子树的关键字保证左小右大的顺序
也就是说，一棵 3 阶的 B 树（即节点最多有三个子树），每个节点的关键字数最少为 1，最多为 2，
如果要添加数据的子树的关键字数已经是最多，就需要拆分节点，调整树的结构。



B+树：
一棵 B+ 树需要满足以下条件：
（1）节点的子树数和关键字数相同（B 树是关键字数比子树数少一）
（2）节点的关键字表示的是子树中的最大数，在子树中同样含有这个数据
（3）叶子节点包含了全部数据，同时符合左小右大的顺序


简单概括下 B+ 树的三个特点：
（1）关键字数和子树相同
（2）非叶子节点仅用作索引，它的关键字和子节点有重复元素
（3）叶子节点用指针连在一起
首先第一点不用特别介绍了，在 B 树中，节点的关键字用于在查询时确定查询区间，因此关键字数比子树数少一；
而在 B+ 树中，节点的关键字代表子树的最大值，因此关键字数等于子树数。
第二点，除叶子节点外的所有节点的关键字，都在它的下一级子树中同样存在，最后所有数据都存储在叶子节点中。
第三点，叶子节点包含了全部的数据，并且按顺序排列，B+ 树使用一个链表将它们排列起来，这样在查询时效率更快。
由于 B+ 树的中间节点不含有实际数据，只有子树的最大数据和子树指针，因此磁盘页中可以容纳更多节点元素，
也就是说同样数据情况下，B+ 树会 B 树更加“矮胖”，因此查询效率更快。

"""