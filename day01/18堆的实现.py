# python语言实现


class Heap:
    def __init__(self, elist):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    # 取堆顶元素
    def peek(self):
        if self.is_empty():
            raise ValueError("堆为空")
        return self._elems[0]

    # 上浮
    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    # 插入
    def push(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    # 下沉
    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i = j
            j = 2 * j + 1
        elems[i] = e

    # 弹出
    def pop(self):
        if self.is_empty():
            raise ValueError("堆为空")
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    # 从数组构建堆
    def buildheap(self):
        end = len(self._elems)
        for i in range(end // 2 - 1, -1, -1):
            self.siftdown(self._elems[i], i, end)