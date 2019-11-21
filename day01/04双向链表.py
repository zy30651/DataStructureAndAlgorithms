class Node(object):
    """双向链表的节点"""
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DLinkList(object):
    """双向链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """返回链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item)
            cur = cur.next
        print("")

    def add(self, item):
        """增加头部节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            # 如果不是空链表
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, item):
        """增加尾部节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def search(self, item):
        """查找一个节点"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

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
            node.prev = cur
            node.next = cur.next
            cur.next = node
            cur.next.prev = node

    def remove(self, item):
        """删除一个节点"""
        if self.is_empty():
            return

        cur = self.__head
        # 若头节点的元素是要查找的元素
        if cur.item == item:
            # 如果这个节点的下一个节点，不是头节点，说明链表不止1个节点
            if cur.next is not None:
                self.__head = cur.next
                self.__head.prev = None
            else:
                # 链表只有一个节点
                self.__head = Node
            return

        while cur is not None:
            if cur.item == item:
                # 将cur的前一个节点的next指向cur的后一个节点
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                break
            cur = cur.next


if __name__ == "__main__":
    ll = DLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:", ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(9))
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
