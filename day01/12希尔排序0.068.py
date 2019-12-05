# 希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种
# 更高效的改进版本。希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。
# 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少
# ，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

"""
基本思想：
将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（
步长更长了，列数更少了）来进行。最后整个表就只有一列了。将数组转换至表是为了
更好地理解这算法，算法本身还是使用数组进行排序。
"""

from day01.utils import time_deco, random_nums
@time_deco
def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = n // 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j >= gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        # 得到新的步长
        gap = gap // 2


if __name__ == '__main__':
    li = random_nums()
    shell_sort(li)

# 0.065秒
