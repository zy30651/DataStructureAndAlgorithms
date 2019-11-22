# 快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），
# 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所
# 有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行
# 以此达到整个数据变成有序序列。

"""
步骤为：
从数列中挑出一个元素，称为"基准"（pivot），
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

最优时间复杂度：O(nlogn)
最坏时间复杂度：O(n2)
稳定性：不稳定
"""

from day01.utils import time_deco, random_nums
@time_deco
def quick_sort(alist, start, end):
    """快速排序"""
    # 递归退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1

        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1

        # 将low指向的放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)


if __name__ == '__main__':
    li = random_nums()
    quick_sort(li)
# 0.026秒
