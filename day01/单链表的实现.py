class SingleNode(object):
    """单链表的节点"""
    def __init__(self, item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标示
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """链接长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print('')

    def add(self, item):
        """头部加入数据"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，
        node.next = self._head
        # 将链接的头_head指向新节点
        self._head = node

    def append(self, item):
        """尾部加入数据"""
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置加入数据"""
        # 如果 <= 0 说明是头部插入
        if pos <= 0:
            self.add(item)
        # 尾部插入
        elif pos > (self.length() -1):
            self.append(item)
        else:
            # 指定位置插入
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置的pos的前一个位置
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 找到指定元素
            if cur.item == item:
                # 第一个节点就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置的前一个节点的next，指向删除位置的后一个节点
                    pre.next = cur.next
            # 没找到，继续后移
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

