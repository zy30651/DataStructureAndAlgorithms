class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SinCycLinkedList(object):
    """单向循环链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """返回链表长度"""
        # 如果链表为空，返回0
        if self.is_empty():
            return 0

        count = 1
        cur = self.__head
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.__head
        print(cur.item)
        while cur.next != self.__head:
            cur = cur.next
            print(cur.item)
        print("")

    def add(self, item):
        """头部添加节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 添加的节点指向_head
            node.next = self.__head
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 当cur.next == self._head的时候，就找到尾部节点了
            cur.next = node
            self.__head = node

    def append(self, item):
        """尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos >= (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            count = 0
            cur = self.__head
            while count < (pos-1):
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除一个节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        # 若头节点的元素是要查找的元素
        if cur.item == item:
            # 如果这个节点的下一个节点，不是头节点，说明链表不止1个节点
            if cur.next != self.__head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self.__head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self.__head.next
                self.__head = self.__head.next
            else:
                # 链表只有一个节点
                self.__head = Node
        else:
            pre = self.__head
            # 第一个节点不是要删除的
            while cur.next != self.__head:
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

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False

        cur = self.__head
        if cur.item == item:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.item == item:
                return True
        return False


if __name__ == "__main__":
    ll = SinCycLinkedList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:", ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(7))
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()






