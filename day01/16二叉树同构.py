# 判断二叉树是否同构
# 同构的意思是：一个节点的儿子节点不变，位置可以变化
# 1：建立二叉树
# 2：判断是否同构


# 二叉树的节点表示以及树的创建
class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


"""
二叉树是根据一个？创建的，例如：
输入给出2棵二叉树树的信息。对于每棵树，首先在一行中给出一个非负整数N (≤)，即该树的结点数
（此时假设结点从0到N−1编号）；随后N行，第i行对应编号第i个结点，给出该结点中存储的1个英文大
写字母、其左孩子结点的编号、右孩子结点的编号。如果孩子结点为空，则在相应位置上给出“-”。
给出的数据间用一个空格分隔。注意：题目保证每个结点中存储的字母是不同的。
8       8
A 1 2   G - 4
B 3 4   B 7 6
C 5 -   F - -
D - -   A 5 1
E 6 -   H - -
G 7 -   C 0 -
F - -   D - -
H - -   E 2 -

输出  YES
本题使用结构数组（静态链表）存储二叉树
结构定义：
"""


# 节点

