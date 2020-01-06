# 二叉树
# 二叉树是每个节点最多有两个子树的树结构。通常子树被称作“左子树”
# （left subtree）和“右子树”（right subtree）
"""
二叉树的性质：
性质1: 在二叉树的第i层上至多有2^(i-1)个结点（i>0）
性质2: 深度为k的二叉树至多有2^k - 1个结点（k>0）
性质3: 对于任意一棵二叉树，如果其叶结点数为N0，而度数为2的结点总数为N2，则N0=N2+1;
性质4:具有n个结点的完全二叉树的深度必为 log2(n+1)
性质5:对完全二叉树，若从上至下、从左至右编号，则编号为i 的结点，其左孩子编号必为2i，
其右孩子编号必为2i＋1；其双亲的编号必为i/2（i＝1 时为根,除外

"""


# 二叉树的节点表示以及树的创建
class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


# 树的创建，创建一个树类，并给一个root根节点，一开始为空，随后添加节点
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

    # 二叉树的遍历
    # 深度遍历-先序遍历：先访问根节点，然后递归使用先序遍历访问左子树，再递归访问右子树
    # 根节点-->左子树-->右子树
    def preorder(self, root):
        """递归实现先序遍历"""
        if root is None:
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    # 中序遍历：先递归使用先序遍历访问左子树，然后访问根节点，再递归访问右子树
    # 左子树-->根节点-->右子树
    def inorder(self, root):
        """递归实现中序遍历"""
        if root is None:
            return
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)

    # 后序遍历 在后序遍历中，我们先递归使用后序遍历访问左子树和右子树，最后访问根节点
    # 左子树->右子树->根节点
    def postorder(self, root):
        """递归实现后续遍历"""
        if root is None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)

    # 广度优先遍历(层次遍历)
    # 从树的root开始，从上到下从从左到右遍历整个树的节点
    def breadth_travel(self):
        """利用队列实现树的层次遍历"""
        if self.root is None:
            return
        queue = list()
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.inorder(tree.root)
    tree.postorder(tree.root)

