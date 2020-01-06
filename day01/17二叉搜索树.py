# 二叉搜索树或二叉排序树、二叉查找树
"""
一颗二叉树，可以为空；如果不为空，则：
1：非空左子树的所有键值小于其根节点的键值
2：非空右子树的所有键值大于其根节点的键值
3：左、右子树都是二叉搜索树
Position Find
Position FindMin
Position FindMax
该页面除了第一个搜索测试没问题之后，后续应该都有错误
"""


class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""

    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root is None:
            self.root = node
        else:
            queue = list()
            queue.append(self.root)
            # 对已有的节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    # 如果左右字数都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    # 递归实现-尾递归，在程序返回的时候才递归,尾递归可以使用循环实现-测试完成
    def position_find_1(self, elem, *args):
        if self is None:
            return
        if len(args) == 0:
            temproot = self.root
        else:
            temproot = args[0]
        if temproot is not None:
            if elem > temproot.elem:
                return self.position_find_1(elem, temproot.rchild)
            elif elem < temproot.elem:
                return self.position_find_1(elem, temproot.lchild)
            else:
                print(temproot.elem)
                return temproot.elem
        else:
            print("节点不存在")

    # 循环实现/迭代函数，查找效率比递归高，效率取决于树的高度
    def position_find_2(self, elem):
        while self:
            if elem > self.root.elem:
                return self.position_find_2(self.root.rchild)
            elif elem < self.root.elem:
                return self.position_find_2(self.root.lchild)
            else:
                return self.root
        return

    # 查找最小值
    def position_find_min(self, *args):
        if self is None:
            return
        elif self.root.lchild is None:
            return self.root
        else:
            elem = None
            if args is not None:
                elem = Node(*args)
            if elem is None:
                elem = self.root
            return self.position_find_min(elem.lchild)

    # 查找最大值
    def position_find_max(self):
        if self is not None:
            elem = self.root.rchild
            while elem is not None:
                elem = elem.rchild
            return elem

    # 插入一个节点
    def insert(self, elem, *args):
        node_tree = Node(*args)
        if self is None:
            self.root = elem
            self.root.lchild = None
            self.root.rchild = None
        else:
            if node_tree is None:
                node_tree = self.root

            if elem < node_tree:
                self.insert(elem, node_tree.lchild)
            elif elem > node_tree:
                self.insert(elem, node_tree.rchild)
        return self

    # 删除一个节点，先找到节点，没找到则递归删除
    # 如果没有儿子可以直接删掉
    # 如果只有1个儿子，则删除节点后，把儿子移到被删除节点位置上
    # 如果有2个儿子，有两种方式
    # 1：在右子树找到最小的值移动到被删除节点位置
    # 2：在左子树找到最大的值移动到被删除节点位置



tree = Tree()
tree.add(30)
tree.add(15)
tree.add(41)
# tree.insert(35)
tree.position_find_2(41)