class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SinCycLinkedList(object):
    """单向循环链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表长度"""
        # 如果链表为空，返回0
        if self.is_empty():
            return 0

        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self._head
        print(cur.item)
        while cur.next != self._head:
            cur = cur.next
            print(cur.item)
        print("")

    def add(self, item):
        """头部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 添加的节点指向_head
            node.next = self._head
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # 当cur.next == self._head的时候，就找到尾部节点了
            cur.next = node
            self._head = node

    def append(self, item):
        """尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            cur.next = node

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if  pos <= 0:
            self.add(item)
        elif pos >= (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            count = 0
            cur = self._head
            while count < (pos-1):
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除一个节点"""
        if self.is_empty():
            return
        cur = self._head
        pre = None
        # 若头节点的元素是要查找的元素
        if cur.item == item:
            # 如果这个节点的下一个节点，不是头节点，说明链表不止1个节点
            if cur.next != self._head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self._head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self._head.next
                self._head = self._head.next
            else:
                # 链表只有一个节点
                self._head = Node
        else:
            pre = self._head
            # 第一个节点不是要删除的
            while cur.next != self._head:
                # 找到了要删除的元素
                if cur.item == item:
                    # 删除
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            if cur.item == item:
                # 尾部删除
                pre.next = cur.next




