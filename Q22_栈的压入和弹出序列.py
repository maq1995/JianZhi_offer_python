# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/9/9 下午2:33
 @desc:
"""
'''
题目:输入两个整数序列,第一个序列表示栈的压入顺序,请判断第二个序列是否为该栈的弹出顺序.假设压入栈的所有数字均不相等,
     例如序列1、2、 3、 4、 5是某栈的压栈顺序，则序列4、 5、 3、 2、 1是该压栈序列对应的一个弹出序列，但4、 3、 5、 1、 2
     就不可能是该压栈序列的弹出序列
     
解析：
    解决这个问题很直观的想法就是建立一个辅助栈，把属兔的第一个序列中的数字依次压入该辅助栈，并按照第二个序列的顺序依次从该栈中
弹出数字。
    以弹出序列4\5\3\2\1为例分析压栈和弹出的过程。第一个希望被弹出的数字是4，因此4需要先压入辅助栈中，压入栈的顺序已经确定，
所以需要将4和4之前的数字全部入栈，此时栈中内容为1\2\3\4，此时4位于栈顶，把4弹出栈后，希望弹出的数字是5，因为5现在不是栈顶
元素，因此将第一个序列中的4以后的数字压入辅助栈中，直到压入数字5为止，此时5位于栈顶，就可以被弹出来了。接下来希望弹出的三个
依次为3\2\1，分别是每次操作的栈顶，直接弹出即可。
    再分析弹出序列4\3\5\1\2.第一希望弹出的数字是4，和上一种情况一样，把4弹出后，3位于栈顶，可以直接弹出，接下来希望弹出的
数字是5,5不是栈顶元素，将第一个序列中的数字压栈，直到将数字5压入栈中，将5弹出后，此时栈顶元素为2，希望弹出的下一个元素是1，
1不是栈顶元素，需要第一个序列中的元素入栈，但是第一个序列中的元素已经全部入栈了，所以下一弹出的元素只能是2，所以该序列不是
第一个序列对应的出栈元素。

    总结：如果下一个希望弹出的数字刚好是栈顶元素，那么直接弹出，如果不是，就把压栈序列中还没有入栈的数字压入辅助栈，直到把
         下一个需要弹出的数字压入栈顶为止，如果所有数字都压入栈了仍然没有找到下一个弹出的数字，那么该序列就不可能是一个弹出序列。
'''


def isPopOrder(pushList, popList):
    if len(pushList) == 0 or len(popList) == 0:
        return False
    stack = []
    while popList:
        pop_data = popList[0]
        if len(stack) > 0 and stack[-1] == pop_data:
            stack.pop()
            popList.pop(0)

        else:  # 栈为空或者栈顶元素不等于pop_data
            while pushList:
                if pushList[0] != pop_data:
                    stack.append(pushList.pop(0))
                else:
                    pushList.pop(0)
                    popList.pop(0)
                    break

        if len(pushList) == 0:
            while stack:
                if stack.pop() != popList.pop(0):
                    return False

    if len(popList) == 0:
        return True
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 3, 2, 1]
list3 = [4, 3, 5, 1, 2]
list4 = []
list5 = []

print isPopOrder(list1, list5)
