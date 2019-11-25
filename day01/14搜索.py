# 搜索是在一个项目集合中找到一个特定项目的算法过程。搜索通常的答案是真的或假的，
# 因为该项目是否存在。 搜索的几种常见方法：顺序查找、二分法查找、二叉树查找、哈希查找


from day01.utils import time_search, random_nums
# 二分查找法-非递归实现
@time_search
def binary_search1(alist, item):
    first = 0
    last = len(alist)-1
    while first <= last:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1
    return False


# 递归实现
@time_search
def binary_search2(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item<alist[midpoint]:
                return binary_search2(alist[:midpoint], item)
            else:
                return binary_search2(alist[midpoint+1:], item)


if __name__ == '__main__':
    li = random_nums()
    li.insert(200001, 0)
    # binary_search1(li, 200001)
    binary_search2(li, 200001)

