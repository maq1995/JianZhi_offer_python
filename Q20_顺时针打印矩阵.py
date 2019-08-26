# encoding: utf-8
"""
 @project:JianZhi_offer
 @author: Ma Qian
 @language:Python 2.7.2 
 @time: 2019/8/23 下午2:56
 @desc:
"""
'''
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
    例如：如果输入如下矩阵：
         1  2  3  4
         5  6  7  8
         9  10 11 12
         13 14 15 16
         则依次打印出来的数据为：1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
         
         可以看出打印是从外圈到内圈的顺序依次打印,我们可以把矩阵想象成若干个圈,用一个循环来打印矩阵,每一次打印矩阵中的一个圈.
         接下来分析循环结束的条件.假设这个矩阵的行数是rows,列数是columns.打印第一圈的左上角的坐标是(0,0),第二圈的左上角坐
         标是(2,2),依次类推,我们注意到,左上角的坐标中行标和列标总是相同的,于是可以在矩阵中选取左上角为(start,start)的一圈
         作为我们分析的目标.
         对于一个5*5的矩阵而言,最后一圈只有一个数字,对应的坐标是(2,2).我们发现,5>2*2.对于一个6*6的矩阵而言,最后一圈有4个数
         字,其左上角坐标仍然为(2,2).我们发现6>2*2依然成立.于是我们得出,让循环继续的条件是columns>2*startX,且rows>2*startY
         所以主流程为:printMatrixClockwisely()
         
         接下来我们考虑如何打印一圈,即如何实现printMatrixInCircle.
         打印一圈分为4步:第一步从左到右打印一行,
                       第二步从上到下打印一列,
                       第三步从右到左打印一行,
                       第四步从下到上打印一列.
         每一步我们根据起始坐标和终止坐标用一个循环就能打印出一行或一列.
         不过值得注意的是,最后一圈可能退化成只有一行\只有一列\甚至只有一个数字.
         为此我们要仔细分析打印时每一步的前提条件:
            第一步总是需要的,因为打印一圈至少需要一步,如果只有一行,那么就不用第二步了,也就是说需要第二步的前提条件是终止行号大于起始行号.
            需要第三步打印的前提条件是圈内至少有两行两列,也就是说除了要求终止行号大于起始行号之外,还要求终止列号大于起始列号.
            同理,需要打印第四步的前提条件是至少有三行两列,因此要求终止行号比起始行号至少大2,同时终止列号大于起始列号.
'''


def printMatrixClockwisely(matrix, columes, rows):
    if len(matrix) == 0 or (columes <= 0 or rows <= 0):
        return

    start = 0
    ret = []
    while columes > start * 2 and rows > start * 2:
        printMatrixInCircle(matrix, columes, rows, start, ret)
        start += 1
    print ret


def printMatrixInCircle(matrix, columns, rows, start, ret):
    endX = columns - 1 - start
    endY = rows - 1 - start

    # 从左到右打印一行
    for i in range(start, endX+1):
        ret.append(matrix[start][i])

    # 从上到下打印一列
    if start < endY:
        for j in range(start+1, endY+1):
            ret.append(matrix[j][endX])

    # 从右到左打印一行
    if start < endX and start < endY:
        for i in range(endX-1, start-1, -1):
            ret.append(matrix[endY][i])

    # 从下到上打印一列
    if start< endX and start < endY-1:
        for i in range(endY-1, start, -1):
            ret.append(matrix[i][start])


# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]

# matrix = [[1, 2, 3, 4]]

# matrix = [[1],
#           [2],
#           [3],
#           [4]]
matrix = [[1]]
rows = len(matrix)
columns = len(matrix[0]) if matrix else 0
printMatrixClockwisely(matrix, columns, rows)

